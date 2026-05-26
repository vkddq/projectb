from django.contrib import admin
from .models import Lesson, Attendance

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'date', 'start_time', 'status')
    list_filter = ('status', 'date', 'teacher')

admin.site.register(Attendance) 