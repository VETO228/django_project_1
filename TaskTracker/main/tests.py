from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import RegisterUser

class RegisterUserModelTest(TestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpass',
            'email': 'testuser@example.com',
            'surname': 'Test Surname',
            'role': 'Developer',
            'projects': 'Project 1, Project 2'
        }
        self.user = RegisterUser.objects.create_user(**self.user_data)

    def test_user_creation(self):
        self.assertEqual(RegisterUser.objects.count(), 1)
        self.assertEqual(self.user.username, self.user_data['username'])
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.surname, self.user_data['surname'])
        self.assertEqual(self.user.role, self.user_data['role'])
        self.assertEqual(self.user.projects, self.user_data['projects'])

    def test_user_str_method(self):
        self.assertEqual(str(self.user), self.user_data['username'])

    def test_unique_email(self):
        with self.assertRaises(ValidationError):
            RegisterUser.objects.create_user(
                username='anotheruser',
                password='anotherpass',
                email=self.user_data['email']
            )

    def test_blank_surname(self):
        user_with_blank_surname = RegisterUser.objects.create_user(
            username='userwithblanksurname',
            password='password',
            email='userwithblanksurname@example.com',
            surname=''
        )
        self.assertEqual(user_with_blank_surname.surname, '')

    def test_avatar_default(self):
        self.assertEqual(self.user.avatar.name,
                         'default_avatar.png')