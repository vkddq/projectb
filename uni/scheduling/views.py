from django.shortcuts import render
from .models import Lesson

def schedule_view(request):
    # Get all scheduled and completed lessons, ordered by date and time
    lessons = Lesson.objects.order_by('-date', 'start_time')
    return render(request, 'schedule.html', {'lessons': lessons})