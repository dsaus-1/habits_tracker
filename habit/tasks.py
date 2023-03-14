from datetime import datetime, timedelta

from celery import shared_task

from habit.models import Habit
from habit.services import send_message_tg

@shared_task
def check_time_habits():
    """Проверка срабатывает каждую минуту, сравнивает текущее время со временем выполнения привычки
     и отправляет уведомление в Телеграме"""
    time_now = datetime.now()
    habit_queryset = Habit.objects.filter(time__hour=time_now.hour, time__minute=time_now.minute)

    for habit in habit_queryset:
        if habit.last_execution:
            time_send = habit.last_execution + timedelta(days=habit.frequency)
            if time_send == time_now.date():

                send_message_tg(habit)
                habit.last_execution = time_now.date()
                habit.save()
        else:
            send_message_tg(habit)
            habit.last_execution = time_now.date()
            habit.save()
