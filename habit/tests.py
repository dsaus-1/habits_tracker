from rest_framework import status
from rest_framework.test import APITestCase

from config import settings
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='test@gmail.com', chat_id=settings.TELEGRAM_TEST_CHAT_ID, phone='9299992929')
        self.user.set_password('159753qwerty')
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": 'test@gmail.com',
                                               "password": "159753qwerty"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


    def test_habit_create(self):

        response = self.client.post('/habit/',
                                    {
                                        "place": "На улице",
                                        "time": "20:00:00",
                                        "action": "поливать огурцы",
                                        "pleasant_habit": False,
                                        "frequency": 1,
                                        "time_to_complete": "00:02:00",
                                        "award": "Выпить чай"
                                    }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_list(self):
        self.test_habit_create()
        response = self.client.get('/habit/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "place": "На улице",
                    "time": "20:00:00",
                    "action": "поливать огурцы",
                    "pleasant_habit": False,
                    "related_habit": None,
                    "frequency": 1,
                    "award": "Выпить чай",
                    "time_to_complete": "00:02:00",
                    "public": True
                }
            ]
        )

    def test_habit_update(self):
        self.test_habit_create()

        response = self.client.put('/habit/5/', {
                                        "place": "В огороде",
                                        "time": "20:00:00",
                                        "action": "поливать огурцы",
                                        "pleasant_habit": False,
                                        "frequency": 1,
                                        "time_to_complete": "00:02:00",
                                        "award": "Выпить чай"
                                    })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "place": "В огороде",
                "time": "20:00:00",
                "action": "поливать огурцы",
                "pleasant_habit": False,
                "related_habit": None,
                "frequency": 1,
                "time_to_complete": "00:02:00",
                "award": "Выпить чай",
                "public": True
            }
        )

    def test_habit_detail(self):
        self.test_habit_create()
        response = self.client.get('/habit/3/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "place": "На улице",
                "time": "20:00:00",
                "action": "поливать огурцы",
                "pleasant_habit": False,
                "related_habit": None,
                "frequency": 1,
                "time_to_complete": "00:02:00",
                "award": "Выпить чай",
                "public": True
            }
        )

    def test_habit_delete(self):
        self.test_habit_create()
        response = self.client.delete('/habit/2/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicHabitTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='test@gmail.com', chat_id=settings.TELEGRAM_TEST_CHAT_ID, phone='9299992929')
        self.user.set_password('159753qwerty')
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": 'test@gmail.com',
                                               "password": "159753qwerty"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.client.post('/habit/',
                         {
                             "place": "На улице",
                             "time": "20:00:00",
                             "action": "поливать огурцы",
                             "pleasant_habit": False,
                             "frequency": 1,
                             "time_to_complete": "00:02:00",
                             "award": "Выпить чай"
                         }
                         )

    def test_public_habit_detail(self):
        response = self.client.get('/habit/6/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "place": "На улице",
                "time": "20:00:00",
                "action": "поливать огурцы",
                "pleasant_habit": False,
                "related_habit": None,
                "frequency": 1,
                "time_to_complete": "00:02:00",
                "award": "Выпить чай",
                "public": True
            }
        )

    def test_public_habit_list(self):
        response = self.client.get('/habit/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "place": "На улице",
                    "time": "20:00:00",
                    "action": "поливать огурцы",
                    "pleasant_habit": False,
                    "related_habit": None,
                    "frequency": 1,
                    "award": "Выпить чай",
                    "time_to_complete": "00:02:00",
                    "public": True
                }
            ]
        )
