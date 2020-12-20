from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_mail = models.EmailField()

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"