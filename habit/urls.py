from django.urls import path
from rest_framework.routers import DefaultRouter

from habit.apps import HabitConfig
from habit.views import HabitModelViewSet
from users.views import UserModelViewSet

app_name = HabitConfig.name
router = DefaultRouter()
router.register(r'habit', HabitModelViewSet, basename='habit')

urlpatterns = router.urls