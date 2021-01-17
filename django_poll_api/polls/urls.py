from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from polls.views import PollListView, PollActionsView, PollCreateView, \
    PollRetrieveView, PollResultsView, QuestionCreateView, QuestionActionsView

urlpatterns = [
    path('', PollListView.as_view()),
    path('poll/add', PollCreateView.as_view()),
    path('poll/<int:pk>', PollRetrieveView.as_view()),
    path('poll/<int:pk>/edit', PollActionsView.as_view()),
    path('poll/results', PollResultsView.as_view()),
    path('poll/add_question', QuestionCreateView.as_view()),
    path('poll/<int:pk>/questions/edit', QuestionActionsView.as_view())

]
#
urlpatterns = format_suffix_patterns(urlpatterns)
