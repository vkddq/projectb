from django.shortcuts import render
from rest_framework import viewsets
from users.permissions import IsAdminOrReadOnly
from .models import Subject, Student, Group
from .serializers import SubjectSerializer, StudentSerializer, GroupSerializer

def students_view(request):
    students = Student.objects.filter(is_active=True)
    groups = Group.objects.filter(is_active=True)
    return render(request, 'academics.html', {'students': students, 'groups': groups})

def grades_view(request):
    return render(request, 'grades.html')

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminOrReadOnly]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('branch').all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]