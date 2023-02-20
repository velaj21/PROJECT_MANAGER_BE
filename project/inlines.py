from django.contrib.admin import TabularInline

from . import models


class ProjectTaskInline(TabularInline):
    model = models.Task
    fields = ['employee', 'sprint']
    autocomplete_fields = ['employee', 'sprint']
    extra = 0
    min_num = 0
    can_delete = True


class EmployeeTaskInline(TabularInline):
    model = models.Task
    fields = ['project', 'sprint']
    autocomplete_fields = ['project', 'sprint']
    extra = 0
    min_num = 0
    can_delete = True


class SprintTaskInline(TabularInline):
    model = models.Task
    fields = ['employee', 'project']
    autocomplete_fields = ['employee', 'project']
    extra = 0
    min_num = 0
    can_delete = True
