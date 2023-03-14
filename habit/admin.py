from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', "place", "time", "action", "pleasant_habit",
                    "related_habit", "frequency", "award", "time_to_complete",
                    "public", "last_execution", "user", )