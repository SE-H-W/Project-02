from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import markdown
from django.core.cache import cache
import os
from django.utils import timezone
from info.models import FavCityEntry, CitySearchRecord, Comment
from django.contrib.messages import get_messages
from unittest.mock import patch, MagicMock
from CityByte.views import initialize_gemini_llm
import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth import get_user_model

class CityInfoViewTests(TestCase):
    def setUp(self):
        self.url = reverse('city_info', kwargs={'city_name': 'New York'})

    @patch('CityByte.views.initialize_gemini_llm')
    def test_city_info_post_api_key_not_set(self, mock_initialize_llm):
        mock_initialize_llm.side_effect = Exception("Gemini API Key not set. Please configure the key.")
        
        response = self.client.post(self.url, {'days': '2'})
        self.assertEqual(response.status_code, 500)  # Expecting 500 for missing API key

    def test_city_info_post_empty_request(self):
        response = self.client.post(self.url, {})  # No data
        self.assertEqual(response.status_code, 400)  # Expecting 400 for bad request due to missing 'days'

    
    def test_city_info_post_missing_days(self):
        response = self.client.post(self.url, {'days': ''})  # Missing 'days'
        self.assertEqual(response.status_code, 400)  # Expecting 400 for empty 'days' parameter

class CityNewsViewTests(TestCase):
    def setUp(self):
        self.url = reverse('city_news', kwargs={'city': 'Paris', 'country': 'FR'})  # Testing with one-word city

    @patch('info.helpers.newsapi_helper.NewsAPIHelper.get_city_news')
    def test_city_news_with_articles_one_word_city(self, mock_get_city_news):
        # Mock the response of the get_city_news method for a one-word city
        mock_get_city_news.return_value = [
            {
                "title": "Top Attractions in Paris",
                "url": "https://news.example.com/paris-attractions",
                "source": {"name": "Paris News Daily"},
                "publishedAt": "2024-10-31T08:00:00Z",
                "description": "Explore the top attractions in Paris, the City of Light."
            }
        ]

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info/news.html')
        
        # Verify that the one-word city name and its articles are correctly rendered
        self.assertContains(response, "Top Attractions in Paris")
        self.assertContains(response, "Paris News Daily")
        self.assertContains(response, "Explore the top attractions in Paris, the City of Light.")
        self.assertContains(response, '<a href="https://news.example.com/paris-attractions" target="_blank">Top Attractions in Paris</a>', html=True)

    @patch('info.helpers.newsapi_helper.NewsAPIHelper.get_city_news')
    def test_city_news_no_articles_one_word_city(self, mock_get_city_news):
        # Mock an empty response for a one-word city to simulate no articles available
        mock_get_city_news.return_value = []

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info/news.html')
        
        # Check that the "No news available" message is displayed for the one-word city
        self.assertContains(response, "No news available for this location.")