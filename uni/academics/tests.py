from django.test import TestCase
from rest_framework.test import APIClient
from branches.models import Branch
from academics.models import Student
from users.models import CustomUser

class StudentPerformanceTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.admin = CustomUser.objects.create_user(
            phone_number='999999999', password='password123', role='ADMIN'
        )
        
        self.branch = Branch.objects.create(name='Tech Campus', city='Kyiv', address='123 St')
        
        for i in range(15):
            Student.objects.create(
                first_name=f'Test{i}', 
                last_name='Student', 
                phone=f'555000{i}', 
                branch=self.branch,
                date_of_birth='2000-01-01',
                email=f'test{i}@example.com'
            )

    def test_student_list_no_n_plus_one(self):
        self.client.force_authenticate(user=self.admin)
        
        with self.assertNumQueries(1):
            response = self.client.get('/api/students/')
            
        self.assertEqual(response.status_code, 200)