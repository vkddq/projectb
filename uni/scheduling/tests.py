from datetime import date
from django.test import TestCase
from academics.models import Subject
from users.models import CustomUser
from branches.models import Branch
from .models import Lesson

class LessonConflictTests(TestCase):
    def setUp(self):
        # 1. ARRANGE: Set up shared data for all tests
        self.branch = Branch.objects.create(name='Main Campus', city='Kyiv', address='123 St')
        self.subject = Subject.objects.create(name='Mathematics', branch=self.branch)
        
        self.teacher = CustomUser.objects.create_user(
            phone_number='1234567890', password='password123', role='TEACHER'
        )
        self.test_date = date(2026, 5, 1)

    def test_overlapping_lessons_are_a_conflict(self):
        Lesson.objects.create(
            subject=self.subject, teacher=self.teacher,
            date=self.test_date, start_time='10:00', end_time='11:00', status='SCHEDULED'
        )
        has_conflict = Lesson.has_conflict(
            teacher=self.teacher, date=self.test_date, 
            start_time='10:30', end_time='11:30'
        )
        self.assertTrue(has_conflict)

    def test_exact_same_time_is_a_conflict(self):
        Lesson.objects.create(
            subject=self.subject, teacher=self.teacher,
            date=self.test_date, start_time='10:00', end_time='11:00', status='SCHEDULED'
        )
        has_conflict = Lesson.has_conflict(
            teacher=self.teacher, date=self.test_date, 
            start_time='10:00', end_time='11:00'
        )
        self.assertTrue(has_conflict)

    def test_back_to_back_lessons_do_not_conflict(self):
        Lesson.objects.create(
            subject=self.subject, teacher=self.teacher,
            date=self.test_date, start_time='10:00', end_time='11:00', status='SCHEDULED'
        )
        has_conflict = Lesson.has_conflict(
            teacher=self.teacher, date=self.test_date, 
            start_time='11:00', end_time='12:00'
        )
        self.assertFalse(has_conflict)

    def test_canceled_lessons_dont_block_new_ones(self):
        # Testing your custom CANCELLED status!
        Lesson.objects.create(
            subject=self.subject, teacher=self.teacher,
            date=self.test_date, start_time='10:00', end_time='11:00', status='CANCELLED'
        )
        has_conflict = Lesson.has_conflict(
            teacher=self.teacher, date=self.test_date, 
            start_time='10:00', end_time='11:00'
        )
        self.assertFalse(has_conflict)