from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from datetime import date


# Create your models here.

class Employee(models.Model):
    full_name = models.CharField(max_length=125)
    email = models.CharField(max_length=125, null=True, blank=True, unique=True)
    password = models.CharField(max_length=125)
    phone_number = models.CharField(max_length=13,
                                    validators=[RegexValidator(r'((\+3556)|(06))[789]\d{7}',
                                                               message='Numri i telefonit nuk eshte i vlefshem!'
                                                               )],
                                    unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name}'


class Project(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Sprint(models.Model):
    sprint_period = models.CharField(max_length=120,
                                     default=f'Periudha e sprintit: {date.today().strftime("%Y-%m")}')
    month_first_day = models.PositiveSmallIntegerField(default=1, editable=False)
    month_last_day = models.PositiveSmallIntegerField(null=True, blank=True, editable=False)

    def __str__(self):
        return f'{self.sprint_period}'


class Task(models.Model):
    sprint = models.ForeignKey(Sprint, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    work_day = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.project} - {self.employee}'
