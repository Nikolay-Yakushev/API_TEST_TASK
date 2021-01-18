from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from polls.views import (
    PollActionsView,
    PollCreateView,
    PollPassView,
    PollResultsView,
    QuestionCreateView,
    QuestionActionsView,
)

urlpatterns = [
    path("polls/", PollCreateView.as_view()),
    path("polls/<int:pk>", PollActionsView.as_view()),
    path("questions/", QuestionCreateView.as_view()),
    path("questions/<int:pk>", QuestionActionsView.as_view()),
    path("polls/<int:pk>/pass/", PollPassView.as_view()),
    path("polls_results/", PollResultsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
