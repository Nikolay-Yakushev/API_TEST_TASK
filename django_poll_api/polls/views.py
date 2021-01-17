from collections import defaultdict

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import F

# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from polls.models import Poll, PollAnswer, PollQuestions, PollQuestionChoice
from polls.serializers import PollSerializer, PollAnswerSerializer, PollQuestionSerializer, PollChoiceSerializer, \
    QuestionSerializer
import random


# Получение списка доступных опросов API for users/admins
class PollListView(generics.ListAPIView):
    queryset = Poll.objects
    serializer_class = PollSerializer


# создание опроса Api for Admins
class PollCreateView(generics.CreateAPIView):
    queryset = Poll.objects
    serializer_class = PollSerializer
    permission_classes = [IsAdminUser]


#  Api for
class PollActionsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.prefetch_related('questions')
    serializer_class = PollSerializer
    permission_classes = [IsAdminUser]


# прхождение опроса :Api for users/admins
class PollRetrieveView(generics.RetrieveAPIView):
    queryset = Poll.objects.prefetch_related('questions')
    serializer_class = PollSerializer

    def post(self, request, *args, **kswargs):
        user_data = request.data
        user = request.user
        if not user.is_authenticated:
            number_ident = str(random.randint(100000, 999999))

            user = User.objects.create_user(username='anonym -' + number_ident,
                                            email=f'anonym@{number_ident}.com',
                                            password=number_ident)
            login(self.request, user)
        print(user_data.items())
        for question_id, question_answer in user_data.items():
            PollAnswer.objects.create(user=user, question_id=question_id, answer=question_answer)
        return Response(status.HTTP_201_CREATED)


# получение списка ответов на вопросы
class PollResultsView(generics.ListAPIView):
    queryset = PollAnswer.objects
    serializer_class = PollAnswerSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user).select_related(
            'question').annotate(
                        poll_id=F('question__poll_id'),
                        poll_name=F('question__poll__title'),
                        question_text=F('question__question_text'),
                        question_type=F('question__question_type'))

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        result = defaultdict(list)
        for item in serializer.data:
            result['poll_id: ' + str(item['poll_id']) + '' + \
                   '; Poll title: ' + item['poll_name']].append(item)
        return Response(result)


# Создать Question for Admins
class QuestionCreateView(generics.CreateAPIView):
    queryset = PollQuestions.objects
    serializer_class = PollQuestionSerializer
    permission_classes = [IsAdminUser]


# todo Хочу сделать выборку вопросов, но не получается их выбрать
class QuestionActionsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PollQuestions.objects
    serializer_class = PollQuestionSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        # получить все вопросы по poll_id
        # Не могу сделать
        queryset = PollQuestions.objects.filter(poll_id=self.kwargs['pk'])
        return queryset
