from django.contrib.auth.hashers import check_password
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from . import models, serializers

# Create your views here.
from rest_framework import viewsets, status


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()

    serializer_class = serializers.ProjectsSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TasksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['employee', 'sprint']
    ordering = ['-sprint']


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['full_name', 'id', 'email']


class SprintViewSet(viewsets.ModelViewSet):
    queryset = models.Sprint.objects.all()
    serializer_class = serializers.SprintsSerializer


@api_view(['POST'])
def authenticated_user(request):
    auth_user_pass = models.Employee.objects.filter(
        email=request.data.get('email')).values('password', 'id').first()
    resp = check_password(request.data.get('password'), auth_user_pass.get(
        'password')) if auth_user_pass else False
    return Response({'resp': resp, 'id': auth_user_pass.get('id')},
                    status=status.HTTP_200_OK if resp else status.HTTP_401_UNAUTHORIZED)
