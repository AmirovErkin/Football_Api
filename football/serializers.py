from rest_framework import serializers
from .models import Game, OldResult, Reminder


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class OldResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldResult
        fields = '__all__'


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
