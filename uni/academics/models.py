from django.db import models
from branches.models import Branch

class Subject(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='subjects')
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('name', 'branch') 

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    parent_email = models.EmailField(blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='students')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Group(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='groups')
    students = models.ManyToManyField(Student, related_name='study_groups')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name