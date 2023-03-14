from rest_framework import serializers

from habit.models import Habit
from habit.validators import AwardValidator, TimeToCompleteValidator, RelatedHabitValidator, FrequencyValidator, \
    PleasantHabitValidator


class RelatedHabitSerializer(serializers.ModelSerializer):
    """Сериализатор для полезных привычек"""
    class Meta:
        model = Habit
        fields = ("action",
                  "time_to_complete",
                  "place"
                  )

class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для всех привычек"""
    #dict_related_habit = RelatedHabitSerializer(many=False, read_only=True, source='related_habit')


    class Meta:
        model = Habit
        fields = ("place",
                  "time",
                  "action",
                  "pleasant_habit",
                  "related_habit",
                  # "dict_related_habit",
                  "frequency",
                  "award",
                  "time_to_complete",
                  "public")

        validators = [
            AwardValidator(field_1='related_habit', field_2='award'),
            TimeToCompleteValidator(field='time_to_complete'),
            RelatedHabitValidator(field='related_habit'),
            FrequencyValidator(field='frequency'),
            PleasantHabitValidator(field='pleasant_habit')
        ]


