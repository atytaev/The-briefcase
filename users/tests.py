from datetime import date

from django.test import TestCase
from django.urls import reverse

from users.forms import CustomUserCreationForm
from users.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            birth_date=date(1990, 1, 1),
            phone_number='1234567890',
            profile_picture='test_picture.jpg'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.birth_date, date(1990, 1, 1))
        self.assertEqual(self.user.phone_number, '1234567890')
        self.assertEqual(self.user.profile_picture, 'test_picture.jpg')

    def test_string_representation(self):
        self.assertEqual(str(self.user), 'testuser')

class CustomUserCreationFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            'username': 'newuser',
            'birth_date': '1995-05-15',
            'phone_number': '9876543210',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {
            'username': '',
            'birth_date': '',
            'phone_number': 'invalid_number',
            'password1': 'short',
            'password2': 'short',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

class UserAuthViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

    def test_register_view_get(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_view_post(self):
        url = reverse('register')
        response = self.client.post(url, {
            'username': 'newuser',
            'password1': 'StrongPassword!2024',
            'password2': 'StrongPassword!2024',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user_login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login_view_get(self):
        url = reverse('user_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_login_view_post(self):
        url = reverse('user_login')
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('film_list'))

    def test_user_logout_view(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('user_logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('film_list'))