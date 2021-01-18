from django.core.management.base import BaseCommand
from polls.models import *


class Command(BaseCommand):
    help = 'Create Polls objects'

    def handle(self, *args, **options):
        Poll.objects.create(title='Президенты США', description='Опрос посвященный президентам США')
        Poll.objects.create(title='Космос', description='Опрос посвященный достижениям человечества в космосе')
        Poll.objects.create(title='Россия', description='Опрос посвященный современной России')

        for poll_instance in Poll.objects.all():
            if poll_instance.title == 'Президенты США':
                question1 = PollQuestions.objects.create(poll_id=poll_instance.id,
                                                         question_text='Как звали первого президента США',
                                                         question_type='choice')

                answer = PollQuestionChoice(question_id=question1.id, content='Авраам Линкольн').save()
                answer = PollQuestionChoice(question_id=question1.id, content='Рональд Рейган').save()
                answer = PollQuestionChoice(question_id=question1.id, content='Барак Обама').save()
                answer = PollQuestionChoice(question_id=question1.id, content='Джордж Вашингтон').save()

                question2 = PollQuestions.objects.create(poll_id=poll_instance.id,
                                                         question_text='Как звали 44 президента США',
                                                         question_type='text')

                question3 = PollQuestions.objects.create(poll_id=poll_instance.id,
                                                         question_text='Кто из президентов США жил в 20 веке',
                                                         question_type='multiple_choice')

                answer = PollQuestionChoice(question_id=question3.id, content='Франклин Рузвельт').save()
                answer = PollQuestionChoice(question_id=question3.id, content='Рональд Рейган').save()
                answer = PollQuestionChoice(question_id=question3.id, content='Гарри Трумэн').save()
                answer = PollQuestionChoice(question_id=question3.id, content='Джон Тайлер').save()
                answer = PollQuestionChoice(question_id=question3.id, content='Джеймс Монро').save()

            if poll_instance.title == 'Космос':
                question1 = PollQuestions.objects.create(poll_id=poll_instance.id,
                                                         question_text='Как звали 2-го человека полетевшего в космос',
                                                         question_type='choice')

                answer = PollQuestionChoice(question_id=question1.id, content='Авраам Линкольн').save()
                answer = PollQuestionChoice(question_id=question1.id, content='Рональд Рейган').save()
                answer = PollQuestionChoice(question_id=question1.id, content='Герман Титов').save()
                answer = PollQuestionChoice(question_id=question1.id, content='Нил Армстронг').save()

                question2 = PollQuestions.objects.create(poll_id=poll_instance.id,
                                                         question_text='Самый мощный космический телескоп',
                                                         question_type='text')

                question3 = PollQuestions.objects.create(poll_id=poll_instance.id,
                                                         question_text='Ракетоносители доставляющие комсмонатов на МКС',
                                                         question_type='multiple choice')

                answer = PollQuestionChoice(question_id=question3.id, content='Союз').save()
                answer = PollQuestionChoice(question_id=question3.id, content='Crew dragon').save()
                answer = PollQuestionChoice(question_id=question3.id, content='Буран').save()
                answer = PollQuestionChoice(question_id=question3.id, content='Одуванчик').save()

            elif poll_instance.title == 'Россия':
                question1 = PollQuestions.objects.create(poll_id=poll_instance.id,
                                                         question_text='Как звали 1-го председателя правителсьва России',
                                                         question_type='text')
