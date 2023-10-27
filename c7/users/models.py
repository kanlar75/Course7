from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    OWNER = 'owner', 'Пользователь'
    ADMIN = 'admin', 'Администратор'


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=250, unique=True,
                              verbose_name='Адрес электронной почты')
    first_name = models.CharField(max_length=100, **NULLABLE,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=100, **NULLABLE,
                                 verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='users/', **NULLABLE,
                               verbose_name='Аватар')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')
    chat_id = models.CharField(**NULLABLE,
                               verbose_name='id_chat в Telegram')
    role = models.CharField(max_length=20, **NULLABLE,
                            choices=UserRoles.choices, default='owner')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
