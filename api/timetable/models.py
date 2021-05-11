from django.db import models
from django.contrib.auth.models import User

class Timetable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    date = models.DateField(verbose_name="Дата занятия")
    start_time = models.TimeField(verbose_name="Время начала занятия")
    end_time = models.TimeField(verbose_name="Время окончания занятия")
    name = models.CharField(verbose_name="Наименование занятия", max_length=255)
    description = models.TextField(verbose_name="Описание занятия")

