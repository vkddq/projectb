from django.contrib import admin
from .models import Subject, Student, Group

admin.site.register(Subject)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'is_active')
    filter_horizontal = ('students',)

class GroupInline(admin.TabularInline):
    model = Group.students.through
    extra = 0
    verbose_name = "Group Enrollment"
    verbose_name_plural = "Group Enrollments"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'branch', 'is_active')
    list_filter = ('branch', 'is_active')
    inlines = [GroupInline]