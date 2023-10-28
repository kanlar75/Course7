from telebot import TeleBot
from celery import shared_task

from config.settings import TELEGRAM_TOKEN
from habits.models import Habit


@shared_task
def send_habit_message(pk):
    """Задача для отправки напоминания пользователю """

    habit = Habit.objects.get(pk=pk)
    bot = TeleBot(TELEGRAM_TOKEN)
    message = f'Нужно выполнить {habit.action} в {habit.time} в {habit.place}'
    print(message)
    bot.send_message(habit.owner.chat_id, message)
