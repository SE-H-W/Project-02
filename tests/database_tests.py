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

class CRUDDatabaseTests(TestCase):
    def setUp(self):
        # Set up a user and initial objects
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_create_city_search_record(self):
        """Test that a CitySearchRecord can be created and saved to the database."""
        record = CitySearchRecord.objects.create(city_name="Amsterdam", country_name="Netherlands")
        self.assertEqual(CitySearchRecord.objects.count(), 1)
        self.assertEqual(record.city_name, "Amsterdam")

    def test_update_city_search_record(self):
        """Test updating an existing CitySearchRecord."""
        record = CitySearchRecord.objects.create(city_name="Paris", country_name="France")
        record.city_name = "Lyon"
        record.save()
        updated_record = CitySearchRecord.objects.get(id=record.id)
        self.assertEqual(updated_record.city_name, "Lyon")

    def test_delete_city_search_record(self):
        """Test deleting a CitySearchRecord from the database."""
        record = CitySearchRecord.objects.create(city_name="Berlin", country_name="Germany")
        record_id = record.id
        record.delete()
        self.assertFalse(CitySearchRecord.objects.filter(id=record_id).exists())

    def test_create_and_retrieve_comment(self):
        """Test that a Comment can be created and retrieved from the database."""
        comment = Comment.objects.create(
            city="Copenhagen", country="Denmark", comment="Wonderful place!", author=self.user
        )
        retrieved_comment = Comment.objects.get(id=comment.id)
        self.assertEqual(retrieved_comment.comment, "Wonderful place!")
        self.assertEqual(retrieved_comment.author, self.user)

    def test_update_comment(self):
        """Test updating an existing Comment in the database."""
        comment = Comment.objects.create(
            city="Stockholm", country="Sweden", comment="Lovely city!", author=self.user
        )
        comment.comment = "Changed my mind, it's amazing!"
        comment.save()
        updated_comment = Comment.objects.get(id=comment.id)
        self.assertEqual(updated_comment.comment, "Changed my mind, it's amazing!")

    def test_delete_comment(self):
        """Test deleting a Comment from the database."""
        comment = Comment.objects.create(
            city="Dublin", country="Ireland", comment="Nice city!", author=self.user
        )
        comment_id = comment.id
        comment.delete()
        self.assertFalse(Comment.objects.filter(id=comment_id).exists())

    def test_create_fav_city_entry(self):
        """Test creating and saving a FavCityEntry."""
        fav_city = FavCityEntry.objects.create(city="Kyoto", country="Japan", user=self.user)
        self.assertEqual(FavCityEntry.objects.count(), 1)
        self.assertEqual(fav_city.city, "Kyoto")

    def test_update_fav_city_entry(self):
        """Test updating a FavCityEntry."""
        fav_city = FavCityEntry.objects.create(city="Rome", country="Italy", user=self.user)
        fav_city.city = "Milan"
        fav_city.save()
        updated_fav_city = FavCityEntry.objects.get(id=fav_city.id)
        self.assertEqual(updated_fav_city.city, "Milan")

    def test_delete_fav_city_entry(self):
        """Test deleting a FavCityEntry from the database."""
        fav_city = FavCityEntry.objects.create(city="Seoul", country="South Korea", user=self.user)
        fav_city_id = fav_city.id
        fav_city.delete()
        self.assertFalse(FavCityEntry.objects.filter(id=fav_city_id).exists())

    def test_retrieve_multiple_records(self):
        """Test retrieving multiple records from the database."""
        CitySearchRecord.objects.create(city_name="Tokyo", country_name="Japan")
        CitySearchRecord.objects.create(city_name="Osaka", country_name="Japan")
        records = CitySearchRecord.objects.all()
        self.assertEqual(records.count(), 2)

    def test_retrieve_filtered_records(self):
        """Test filtering records by a specific field value."""
        CitySearchRecord.objects.create(city_name="Los Angeles", country_name="USA")
        CitySearchRecord.objects.create(city_name="San Francisco", country_name="USA")
        usa_records = CitySearchRecord.objects.filter(country_name="USA")
        self.assertEqual(usa_records.count(), 2)

    def test_save_multiple_comments_same_city(self):
        """Test saving multiple comments for the same city by the same user."""
        Comment.objects.create(city="Paris", country="France", comment="Amazing!", author=self.user)
        Comment.objects.create(city="Paris", country="France", comment="So beautiful!", author=self.user)
        self.assertEqual(Comment.objects.filter(city="Paris", country="France", author=self.user).count(), 2)