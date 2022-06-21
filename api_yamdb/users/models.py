from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from api_yamdb.settings import LENGTH_TEXT

from .enums import UserRoles


class User(AbstractUser):
    """Класс пользователей."""

    username = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        unique=True,
        db_index=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Имя пользователя содержит недопустимый символ'
        )]
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='email',
        unique=True
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='имя',
        blank=True
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='фамилия',
        blank=True
    )
    bio = models.TextField(
        verbose_name='биография',
        blank=True
    )
    role = models.CharField(
        max_length=UserRoles.max_lenth_choices(),
        verbose_name='роль',
        choices=UserRoles.choices(),
        default=UserRoles.user.name
    )
    confirmation_code = models.CharField(
        max_length=150,
        verbose_name='код подтверждения',
        null=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def __str__(self):
        return self.username[:LENGTH_TEXT]
