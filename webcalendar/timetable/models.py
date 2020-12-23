from django.db import models
from registration.models import User
# Create your models here.

class BaseDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_start = models.TimeField()
    case_end = models.TimeField()
    case = models.CharField(max_length=50)
    case_description = models.TextField()
    is_default = models.BooleanField()

    def __str__(self):
        #return str([self.user, self.case_start, self.case_end, self.case, self.case_description])
        return str(self.user)
        

class Monday(BaseDay):
    class Meta:
        verbose_name = "1 Понедельник"
        verbose_name_plural = "1 Понедельник"

class Tuesday(BaseDay):
    class Meta:
        verbose_name = "2 Вторник"
        verbose_name_plural = "2 Вторник"

class Wednesday(BaseDay):
    class Meta:
        verbose_name = "3 Среда"
        verbose_name_plural = "3 Среда"

class Thursday(BaseDay):
    class Meta:
        verbose_name = "4 Четверг"
        verbose_name_plural = "4 Четверг"

class Friday(BaseDay):
    class Meta:
        verbose_name = "5 Пятница"
        verbose_name_plural = "5 Пятница"
    
class Saturday(BaseDay):
    class Meta:
        verbose_name = "6 Суббота"
        verbose_name_plural = "6 Суббота"

class Sunday(BaseDay):
    class Meta:
        verbose_name = "7 Воскресенье"
        verbose_name_plural = "7 Воскресенье"