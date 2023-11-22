from rest_framework import generics
from .models import Game, OldResult, Reminder
from .serializers import GameSerializer, OldResultSerializer, ReminderSerializer


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class OldResultList(generics.ListCreateAPIView):
    serializer_class = OldResultSerializer

    def get_queryset(self):
        return OldResult.objects.select_related('game').all()


class ReminderList(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
