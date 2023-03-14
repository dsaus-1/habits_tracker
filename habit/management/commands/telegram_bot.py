from django.core.management.base import BaseCommand
from telebot import TeleBot

from config import settings

bot = TeleBot(token=settings.TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	"""Отправка приветственного сообщения в ТГ"""
	bot.reply_to(message, f"Добро пожаловать!\nВаш ID: {message.chat.id}\n(введите его для продолжения регистрации на сайте)")

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		"""Запуск ТГ бота"""

		bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
		bot.load_next_step_handlers()  # Загрузка обработчиков
		bot.infinity_polling()  # Бесконечный цикл бота
