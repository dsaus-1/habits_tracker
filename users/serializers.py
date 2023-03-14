from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для CRUD механизма своего профиля"""

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'chat_id',
            'phone',
            'password'
        )

    def validate_password(self, value):
        return make_password(value)


class AllUserSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра чужих профилей"""

    class Meta:
        model = User
        fields = (
            'email',
            'phone'
        )