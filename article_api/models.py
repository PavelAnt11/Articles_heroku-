from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    group = models.CharField(default='subscriber', max_length=64)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Articles(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

# 1) from django.contrib.auth import get_user_model
# 2) user_model = get_user_model()
# 3) user_model(email='your_email,group='author',password='your_password').save()
