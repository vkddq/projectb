from rest_framework import serializers
from .models import Subject, Student, Group
from branches.serializers import BranchSerializer

class SubjectSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name', read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'branch', 'branch_name', 'is_active']

class StudentSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name', read_only=True)

    class Meta:
        model = Student
        fields = [
            'id', 'first_name', 'last_name', 'date_of_birth', 
            'phone', 'email', 'address', 
            'branch', 'branch_name', 'is_active'
        ]

class GroupSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.name', read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'branch', 'branch_name', 'students', 'is_active']