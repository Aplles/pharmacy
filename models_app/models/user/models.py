from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """Overriding the User model with the email field as primary"""

    username = models.CharField(
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        }, verbose_name="Username",
        unique=True,
    )
    group = models.CharField(max_length=255, blank=True, null=True, verbose_name='Группа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        app_label = "models_app"
        verbose_name = 'User'
        verbose_name_plural = 'Users'