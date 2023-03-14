from rest_framework.test import APITestCase
from rest_framework import status

from config import settings
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='test@gmail.com', chat_id=settings.TELEGRAM_TEST_CHAT_ID, phone='9299992929')
        self.user.set_password('159753qwerty')
        self.user.save()

        response = self.client.post('/users/api/token/', {"email": 'test@gmail.com',
                                               "password": "159753qwerty"})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def tearDown(self):
        super().tearDown()


    def test_user_create(self):
        response = self.client.post('/users/',
                                    {"email": "test123@gmail.com",
                                     "password": "159753qwerty",
                                     "phone": '9299992929',
                                     "chat_id": settings.TELEGRAM_TEST_CHAT_ID}
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_list(self):
        response = self.client.get('/users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "email": "test@gmail.com",
                    "phone": '9299992929'
                }
            ]
            )

    def test_user_update(self):
        response = self.client.put('/users/13/', {"email": "test@gmail.com",
                                                 "chat_id": settings.TELEGRAM_TEST_CHAT_ID,
                                                 "phone": "132132132",
                                                 'password': User.objects.filter(email="test@gmail.com").first().password})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
                {
                    "id": 13,
                    "email": "test@gmail.com",
                    "chat_id": settings.TELEGRAM_TEST_CHAT_ID,
                    "phone": "132132132",
                    'password': response.json().get("password")
                }
        )

    def test_user_detail(self):
        response = self.client.get('/users/11/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "id": 11,
                "email": "test@gmail.com",
                "chat_id": settings.TELEGRAM_TEST_CHAT_ID,
                "phone": "9299992929",
                'password': response.json().get("password")
            }
        )

    def test_user_delete(self):
        response = self.client.delete('/users/10/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ChatIDTestCase(APITestCase):

    def test_chat_id(self):
        response = self.client.get('/users/chat_id/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "url": "t.me/push_habbit_bot",
            }
        )
