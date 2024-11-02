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

class ItineraryViewTests(TestCase):
    def test_itinerary_view_with_itinerary_content(self):
        # Test when the itinerary exists for the city using a POST request
        response = self.client.post(reverse('city_info', args=['Atlanta']), {
            'days': '3'
        })
        
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check that the template used is itinerary.html
        self.assertTemplateUsed(response, 'info/itinerary.html')
        
        # Check that the context contains the correct city name and itinerary content
        self.assertContains(response, 'Itinerary for Atlanta')  # Checks that the city name appears in the template

    
    def test_itinerary_view_css_classes(self):
        # Test that the CSS classes and styles are applied correctly
        response = self.client.post(reverse('city_info', args=['Paris']), {
            'days': '3'
        })
        
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check specific CSS classes used in the template
        self.assertContains(response, 'container my-5')
        self.assertContains(response, 'section bg-light p-5 rounded shadow-lg')
        self.assertContains(response, 'section-heading text-center font-weight-bold mb-4')
        self.assertContains(response, 'itinerary-content text-dark')
