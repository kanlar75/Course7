import datetime

from django.utils import timezone


def send_tg_message(habit):
    """Проверка на наличие логов, их запись и отправка сообщения
    пользователю """

    now = timezone.now()

    if habit.last_reminder:
        if habit.last_reminder <= now - datetime.timedelta(
                days=habit.periodicity):
            habit.last_reminder = timezone.now()
            print("Last reminder - ", habit.last_reminder)
            habit.save()

    else:
        if habit.time <= now.time():
            habit.last_reminder = timezone.now()
            habit.save()
