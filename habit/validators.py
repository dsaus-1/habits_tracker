from datetime import time
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from habit.models import Habit


class AwardValidator:

    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        related_habit = value.get('related_habit')
        award = value.get('award')
        pleasant_habit = value.get('pleasant_habit')

        if related_habit is not None and award is not None:
            raise serializers.ValidationError("Нельзя одновременно выбирать приятную привычку и вознаграждение")

        elif not pleasant_habit:
            if related_habit is None and award is None:
                raise serializers.ValidationError("Необходимо выбрать приятную привычку или вознаграждение")


class TimeToCompleteValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_complete = value.get('time_to_complete')

        if time_to_complete > time(minute=2):
            raise serializers.ValidationError("Время выполнения не может быть больше 2 минут")

class RelatedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get('related_habit')

        if related_habit:
            obj = get_object_or_404(Habit, pk=related_habit.pk)
            if not obj.pleasant_habit:
                raise serializers.ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки")


class PleasantHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        pleasant_habit = value.get('pleasant_habit')
        related_habit = value.get('related_habit')
        award = value.get('award')

        if pleasant_habit:
            if related_habit is not None or award is not None:
                raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки")

class FrequencyValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        frequency = value.get('frequency')

        if frequency:
            if frequency > 7:
                raise serializers.ValidationError("Периодичность не может быть более 7 дней")

