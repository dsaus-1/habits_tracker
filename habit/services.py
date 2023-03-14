from telebot import TeleBot

from config import settings


def send_message_tg(obj):
    """Отправка сообщения в ТГ"""
    bot = TeleBot(settings.TELEGRAM_TOKEN)
    reward = ""
    if obj.related_habit:
        reward = f"\n\nВыполнил привычку?\nТвоя награда: {obj.related_habit.action}\nМесто: {obj.related_habit.place}\n" \
                 f"Продолжительность: {obj.related_habit.time_to_complete}"
    elif obj.award:
        reward = f"\n\nВыполнил привычку?\nТвоя награда: {obj.award}"

    text = f"{obj.user.chat_id} почта: {obj.user.email}\nПришло время выполнить привычку!\nМесто: {obj.place}\n" \
           f"Время: {obj.time}\nПродолжительность: {obj.time_to_complete}\nПривычка: {obj.action}{reward}"

    bot.send_message(obj.user.chat_id, text)