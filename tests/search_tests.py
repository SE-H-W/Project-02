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

class SearchPageViewTests(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.search_url = reverse('main_page')
    
    def test_search_page_render(self):
        # Test if the search page renders successfully for an authenticated user
        response = self.client.get(self.search_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/search.html')

class CitySearchRecordTests(TestCase):
    def setUp(self):
        CitySearchRecord.objects.create(city_name='Paris', country_name='France')

    def test_create_city_search_record(self):
        record = CitySearchRecord.objects.create(city_name='Paris', country_name='France')
        self.assertIsInstance(record, CitySearchRecord)
        self.assertEqual(record.city_name, 'Paris')
        self.assertEqual(record.country_name, 'France')

    def test_city_search_record_str(self):
        record = CitySearchRecord.objects.create(city_name='Paris', country_name='France')
        self.assertEqual(str(record), 'Paris-France')

    def test_create_city_search_record_with_empty_city(self):
        with self.assertRaises(ValidationError):
            record = CitySearchRecord(city_name='', country_name='Germany')
            record.full_clean()  # This will validate the instance

    def test_create_city_search_record_with_empty_country(self):
        with self.assertRaises(ValidationError):
            record = CitySearchRecord(city_name='Berlin', country_name='')
            record.full_clean()  # This will validate the instance
