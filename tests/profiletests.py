from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
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
import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth import get_user_model

class ProfilePageViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile_url = reverse('profile_page')

    def test_profile_page_render_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='password')
        
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')
        
        # Verify the username appears in the page
        self.assertContains(response, 'Hi, Testuser')
        self.assertContains(response, 'Your Favourite Cities')
        self.assertContains(response, 'Top 10 Popular Cities')

    def test_profile_page_render_unauthenticated_user(self):
        # Access profile page without login
        response = self.client.get(self.profile_url)
        
        # Should redirect to login page since the user is not authenticated
        self.assertEqual(response.status_code, 302)  # 302 redirect status
        self.assertIn(reverse('login'), response.url)  # Redirect to login page

    def test_profile_page_with_favorite_cities(self):
        # Create favorite cities for the user
        FavCityEntry.objects.create(user=self.user, city="Paris", country="France")
        FavCityEntry.objects.create(user=self.user, city="Tokyo", country="Japan")
        
        
        self.client.login(username='testuser', password='password')
        
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        
        # Check that favorite cities are displayed
        self.assertContains(response, 'Paris, France')
        self.assertContains(response, 'Tokyo, Japan')
        
    
    def test_profile_page_no_favorite_cities(self):
        # Log in the user
        self.client.login(username='testuser', password='password')
        
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        
        # Check that the empty message for favorite cities is displayed
        self.assertContains(response, "You don't have any favourite cities yet. Start exploring!")

    def test_profile_page_no_popular_cities(self):
        # Log in the user
        self.client.login(username='testuser', password='password')
        
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        
        # Check that the empty message for popular cities is displayed
        self.assertContains(response, "Looks like no popular cities yet. Keep exploring!")
