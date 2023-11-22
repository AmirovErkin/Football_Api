from django.urls import path
from .views import GameList, OldResultList, ReminderList

urlpatterns = [
    path('', GameList.as_view(), name='game-list'),
    path('old-results/', OldResultList.as_view(), name='old-result-list'),
    path('reminders/', ReminderList.as_view(), name='reminder-list'),
]
