from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ test creating new user with email """
        email = 'test@test.com'
        password = 'root'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """ test email for new user is normalized """
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'root')
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """ creating user with no email error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
    
    def test_create_new_superuser(self):
        """ creatin new super user """
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'root'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)