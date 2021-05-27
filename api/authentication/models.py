from django.db import models

class ProxyUser(models.Model):
    picture_url = models.CharField(verbose_name="Аватарка", max_length=255)
    username = models.CharField(verbose_name="Никнейм", max_length=255)
    email = models.EmailField(verbose_name="email")
    first_name = models.CharField(verbose_name="Имя", blank=True, default="None", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", blank=True, default="None", max_length=255)
    password = models.CharField(max_length=200, blank=True)
