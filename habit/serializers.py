from collections import OrderedDict

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


class HabitField(serializers.PrimaryKeyRelatedField):

    def to_representation(self, value):
        id = super(HabitField, self).to_representation(value)
        try:
          habit = Habit.objects.get(pk=id)
          serializer = RelatedHabitSerializer(habit)
          return serializer.data
        except Habit.DoesNotExist:
            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}

        return OrderedDict([(item.id, self.display_value(item)) for item in queryset])


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для всех привычек"""
    public = serializers.BooleanField(allow_null=True, default=True)
    related_habit = HabitField(queryset=Habit.objects.all())


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


