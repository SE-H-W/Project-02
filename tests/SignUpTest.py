from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import markdown
from django.core.cache import cache
import os
from django.utils import timezone
#import dotenv
from info.models import FavCityEntry, CitySearchRecord, Comment
from django.contrib.messages import get_messages
#from dotenv import load_dotenv
from unittest.mock import patch, MagicMock
from CityByte.views import initialize_gemini_llm
from unittest.mock import patch, MagicMock
from info.models import FavCityEntry, CitySearchRecord, Comment
import pytest
from unittest.mock import patch
from info.models import FavCityEntry, CitySearchRecord, Comment
from django.core.exceptions import ValidationError
from info.models import FavCityEntry, Comment, CitySearchRecord
from django.db import IntegrityError
from django.contrib.auth import get_user_model

class SignUpViewTests(TestCase):
    def test_signup_view_get(self):
        # Test if the GET request to the signup page returns a status code 200
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_view_post_valid(self):
        # Test if a valid POST request redirects and creates a new user
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Password123!',
            'password2': 'Password123!',
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect on successful signup
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertEqual(User.objects.get(username='testuser').email, 'testuser@example.com')

    def test_signup_view_post_invalid_password_mismatch(self):
        # Test if an invalid POST request due to password mismatch re-renders the form with errors
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Password123!',
            'password2': 'differentpassword',
        })
        self.assertEqual(response.status_code, 200)  # Should re-render the form

        # Fetch the form from the response context and check for errors
        form = response.context.get('form')
        self.assertIsNotNone(form)  # Ensure the form is in the context
        self.assertFalse(form.is_valid())  # Form should be invalid
        self.assertIn('password2', form.errors)  # Check that 'password2' has an error
        print(form.errors)
        self.assertEqual(form.errors['password2'], ['The two password fields didn’t match.'])

    def test_signup_view_post_invalid_username_taken(self):
        # Test if an invalid POST request due to existing username returns errors
        User.objects.create_user(username='testuser', email='testuser@example.com', password='Password123!')
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'newuser@example.com',
            'password1': 'Password123!',
            'password2': 'Password123!',
        })
        self.assertEqual(response.status_code, 200)  # Should re-render the form

        # Fetch the form from the response context and check for errors
        form = response.context.get('form')
        self.assertIsNotNone(form)  # Ensure the form is in the context
        self.assertFalse(form.is_valid())  # Form should be invalid
        self.assertIn('username', form.errors)  # Check that 'username' has an error
        self.assertEqual(form.errors['username'], ["A user with that username already exists."])

    def test_signup_view_get(self):
        # Test if the GET request to the signup page returns a status code 200
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_view_post_valid(self):
        # Test if a valid POST request redirects and creates a new user
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Password123!',
            'password2': 'Password123!',
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect on successful signup
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertEqual(User.objects.get(username='testuser').email, 'testuser@example.com')
    
    def test_signup_view_post_invalid_email_taken(self):
        # Test if an invalid POST request due to existing email returns errors
        User.objects.create_user(username='testuser', email='testuser@example.com', password='Password123!')
        response = self.client.post(reverse('signup'), {
            'username': 'testuser1',
            'email': 'testuser@example.com',
            'password1': 'Password123!',
            'password2': 'Password123!',
        })
        self.assertEqual(response.status_code, 200)  # Should re-render the form

class SignUpTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.common_passwords = {"password", "12345678", "qwerty", "abc12345", "letmein"}

    def is_common_password(self, password):
        return password.lower() in self.common_passwords

    def test_signup_password_too_short(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'short',
            'password2': 'short'
        })
        self.assertContains(response, "This password is too short. It must contain at least 8 characters.")

    def test_signup_password_numeric_only(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': '12345678',
            'password2': '12345678'
        })
        self.assertContains(response, "This password is entirely numeric.")

    def test_signup_password_same_as_username(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'testuser',
            'password2': 'testuser'
        })
        self.assertContains(response, "The password is too similar to the username.")

    def test_signup_password_same_as_email(self):
        response = self.client.post(reverse('signup'), {
            'email': 'testuser@1.com',
            'password1': 'testuser@1.com',
            'password2': 'testuser@1.com'
        })
        self.assertContains(response, "The password is too similar to the email address.")

    def test_signup_password_common(self):
        for common_password in self.common_passwords:
            response = self.client.post(reverse('signup'), {
                'username': 'testuser',
                'password1': common_password,
                'password2': common_password
            })
            self.assertContains(response, "This password is too common")
    
    def test_signup_empty_username(self):
        response = self.client.post(reverse('signup'), {
            'username': '',
            'password1': 'ValidPass123!',
            'password2': 'ValidPass123!'
        })
        self.assertEqual(response.status_code, 200)  # Form should not be submitted
        self.assertContains(response, 'This field is required.')  # Error message check

    def test_signup_empty_password1(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'Password123!',
            'password2': ''
        })
        self.assertEqual(response.status_code, 200)  # Form should not be submitted
        self.assertContains(response, 'This field is required.')  # Error message check

    def test_signup_empty_password2(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': '',
            'password2': 'Password123!'
        })
        self.assertEqual(response.status_code, 200)  # Form should not be submitted
        self.assertContains(response, 'This field is required.')  # Error message check
    
    def test_signup_username_too_long(self):
        long_username = 'u' * 151  # 151 characters long
        response = self.client.post(reverse('signup'), {
            'username': long_username,
            'password1': 'ValidPassword123!',
            'password2': 'ValidPassword123!'
        })
        
        # Check that the response is a 200 (form is re-rendered)
        self.assertEqual(response.status_code, 200)
        
        # Check that the user was not created
        self.assertFalse(User.objects.filter(username=long_username).exists())
        
        # Check that the form contains the error for the username field
        form = response.context['form']
        self.assertTrue(form.errors['username'])
        self.assertIn('Ensure this value has at most 150 characters (it has 151).', form.errors['username'])
        
    def test_login_empty_username(self):
        response = self.client.post(reverse('login'), {
            'username': '',
            'password': 'ValidPass123!'
        })
        self.assertEqual(response.status_code, 200)  # Form should not be submitted
        self.assertContains(response, 'This field is required.')  # Error message check

    def test_login_empty_password(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': ''
        })
        self.assertEqual(response.status_code, 200)  # Form should not be submitted
        self.assertContains(response, 'This field is required.')  # Error message check

    def test_forgot_password_empty_email(self):
        response = self.client.post(reverse('password_reset'), {
            'email': ''  # Empty email
        })
        self.assertEqual(response.status_code, 200)  # Form should not redirect, stays on the same page
        # Check that the appropriate error message or behavior is enforced
        self.assertContains(response, "This field is required.", html=True)  # Assuming the error message is shown

