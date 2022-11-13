from urllib import request
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from .models import Trivia, Category
from .serializer import TriviaSerializer, CategorySerializer, QuestionSerializer
from rest_framework.response import Response
from trivia import views
import json
import collections


# Create your tests here.
class thing(TestCase):
    def setUp(self):
      Category.objects.create(name='Math', slug='math')
      Category.objects.create(name='Poetry', slug='poetry')
      Trivia.objects.create(name='Trivia', questions='1', slug='trivia', category_id='1', description='Hi')
      Trivia.objects.create(name='math', questions='1', slug='math', category_id='1', description='Hi')

    def test_trivia(self):
      client = APIClient()

      api_call = "/api/v1/trivias/{}/".format(1)
      response = client.get(api_call, format='json')
      response = response.data

      for item in response:
        self.assertEquals(item['name'],'trivia')

    def test_category(self):
      client = APIClient()

      api_call = "/api/v1/category/{}/".format(1)
      response = client.get(api_call, format='json')
      response = response.data

      for item in response:
        self.assertEquals(item['name'],'Math')

    def test_categories(self):
      client = APIClient()
      api_call = "/api/v1/trivias/display-categories/"
      response = client.get(api_call, format='json')
      response = response.data

      count = 0
      for item in response:
        count += 1
      self.assertEquals(count, 2)
