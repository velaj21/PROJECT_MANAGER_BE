from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register(r'tasks', views.TaskViewSet, basename='tasks')
router.register(r'employees', views.EmployeeViewSet, basename='employees')
router.register(r'projects', views.ProjectViewSet, basename='projects')
router.register(r'sprints', views.SprintViewSet, basename='sprints')

task_router = routers.NestedSimpleRouter(router, r'tasks', lookup='sprint')
task_router.register(r'sprint', views.SprintViewSet, basename='sprint')

employee_router = routers.NestedSimpleRouter(
    router, r'tasks', lookup='employee')
employee_router.register(
    r'employee', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(task_router.urls)),
    path(r'', include(employee_router.urls)),
    path(r'auth/', views.authenticated_user)
]
