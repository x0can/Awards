from django.test import TestCase
from .models import *
import unittest
from django.contrib.auth.models import User
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.profile_test = Profile(image='download.png', 
                                    user_id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))




