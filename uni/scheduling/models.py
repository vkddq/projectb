from django.db import models
from django.conf import settings
from academics.models import Subject, Student, Group

class Lesson(models.Model):
    STATUS_CHOICES = (
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lessons')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True, related_name='individual_lessons')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='group_lessons')
    
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='SCHEDULED')

    @classmethod
    def has_conflict(cls, teacher, date, start_time, end_time):
        conflicting_lessons = cls.objects.filter(
            teacher=teacher,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exclude(status='CANCELLED')
        
        return conflicting_lessons.exists()

    def __str__(self):
        return f"{self.subject} on {self.date} at {self.start_time}"


class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='attendance_records')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('lesson', 'student') 

    def __str__(self):
        return f"{self.student} - {'Present' if self.is_present else 'Absent'}"
    
    
    