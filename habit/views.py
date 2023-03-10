from rest_framework.viewsets import ModelViewSet

from habit.models import Habit
from habit.serializers import HabitSerializer


class HabitModelViewSet(ModelViewSet):
    """Контроллер для работы с привычками"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



