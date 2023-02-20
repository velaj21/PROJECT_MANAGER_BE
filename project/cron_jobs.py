from . import models
import calendar
from datetime import date


def add_new_sprint_plan():
    today = date.today()
    _, last_day = calendar.monthrange(today.year, today.month)
    sprint = models.Sprint(month_last_day=last_day)
    sprint.save()
