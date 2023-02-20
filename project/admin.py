from django.contrib import admin

from . import models
from . import inlines
from django_object_actions import DjangoObjectActions, takes_instance_or_queryset
from django.http import HttpResponseRedirect

admin.site.site_header = 'Paneli i administrimit'
admin.site.index_title = 'DDCITY MANAGER'


def record_iteration_util(url, obj, queryset, model, unit):
    next_object = queryset.id + unit if model.objects.filter(
        pk=queryset.id + unit).exists() else model.objects.last().id
    host = obj.headers.get('Host') + url + str(next_object)
    return f'{obj.scheme}://{host}/change/'


# Register your models here.
@admin.register(models.Project)
class AdminProject(DjangoObjectActions, admin.ModelAdmin):
    search_fields = ('name',)
    change_actions = ['previous_record', 'next_record']
    url_name = '/project/project/'
    inlines = [inlines.ProjectTaskInline]

    def previous_record(self, obj, queryset):
        current_index = record_iteration_util(
            self.url_name, obj, queryset, models.Project, -1)
        return HttpResponseRedirect(current_index)

    def next_record(self, obj, queryset):
        current_index = record_iteration_util(
            self.url_name, obj, queryset, models.Project, 1)
        return HttpResponseRedirect(current_index)


@admin.register(models.Employee)
class AdminEmployee(DjangoObjectActions, admin.ModelAdmin):
    search_fields = ('full_name', 'email')
    change_actions = ['previous_record', 'next_record']
    url_name = '/project/employee/'
    inlines = [inlines.EmployeeTaskInline]

    def previous_record(self, obj, queryset):
        current_index = record_iteration_util(
            self.url_name, obj, queryset, models.Employee, -1)
        return HttpResponseRedirect(current_index)

    def next_record(self, obj, queryset):
        current_index = record_iteration_util(
            self.url_name, obj, queryset, models.Employee, 1)
        return HttpResponseRedirect(current_index)


@admin.register(models.Sprint)
class AdminSprint(DjangoObjectActions, admin.ModelAdmin):
    search_fields = ('sprint_period',)
    change_actions = ['previous_record', 'next_record']
    url_name = '/project/sprint/'
    inlines = [inlines.SprintTaskInline]

    def previous_record(self, obj, queryset):
        current_index = record_iteration_util(
            self.url_name, obj, queryset, models.Sprint, -1)
        return HttpResponseRedirect(current_index)

    def next_record(self, obj, queryset):
        current_index = record_iteration_util(
            self.url_name, obj, queryset, models.Sprint, 1)
        return HttpResponseRedirect(current_index)

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.Task)
class AdminTask(DjangoObjectActions, admin.ModelAdmin):
    search_fields = ('description',)
    list_select_related = ('sprint', 'employee', 'project')
    autocomplete_fields = ('sprint', 'employee', 'project')

    change_actions = ['previous_record', 'next_record']
    url_name = '/project/task/'

    def previous_record(self, obj, queryset):
        current_index = record_iteration_util(
            self.url_name, obj, queryset, models.Task, -1)
        return HttpResponseRedirect(current_index)

    def next_record(self, obj, queryset):
        current_index = record_iteration_util(
            self.url_name, obj, queryset, models.Task, 1)
        return HttpResponseRedirect(current_index)
