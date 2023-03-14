from rest_framework.routers import DefaultRouter

from habit.apps import HabitConfig
from habit.views import HabitModelViewSet, PublicHabitReadOnlyModelViewSet

app_name = HabitConfig.name
router = DefaultRouter()
router.register(r'habit', HabitModelViewSet, basename='habit')
router.register(r'public_habit', PublicHabitReadOnlyModelViewSet, basename='public_habit')

urlpatterns = router.urls