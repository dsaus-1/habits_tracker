from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Модель для юзеров"""

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=25, verbose_name='номер телефона')
    chat_id = models.CharField(max_length=10, verbose_name='Чат ID телеграма')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'