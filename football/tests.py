from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Game


class GameListTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_game_list(self):
        url = reverse('game-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_game(self):
        url = reverse('game-list')
        data = {'date': '2023-01-01', 'teams': 'Arsenal : Liverpool', 'result': '2-1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class OldResultListTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_old_result_list(self):
        url = reverse('old-result-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_old_result(self):
        url = reverse('old-result-list')
        game = Game.objects.create(date='2022-01-01', teams='Barcelona : Real Madrid', result='1-1')
        data = {'team': 'Barcelona', 'result': '1-1', 'game': game.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReminderListTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_reminder_list(self):
        url = reverse('reminder-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_reminder(self):
        url = reverse('reminder-list')
        game = Game.objects.create(date='2022-11-09', teams='Barcelona : Real Madrid', result='3 : 2')
        data = {'email': 'mrotabek@gmail.com', 'game': game.id, 'link': 'https://www.youtube.com/watch?v=7MAo4gm5yNo'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
