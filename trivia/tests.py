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
    def setup(self):
        Trivia.objects.create(name='trivia', questions='1', slug='trivia', category_id='1', description='Hi')
        Trivia.objects.create(name='math', questions='1', slug='math', category_id='2', description='Hi')

    def test_trivia(self):
      Category.objects.create(name='Math')
      Category.objects.create(name='Poetry')
      Trivia.objects.create(name='math', questions='1', slug='math', category_id='1', description='less annoying math')
      Trivia.objects.create(name='algerba', questions='1', slug='algebra', category_id='1', description='annoying math')
      Trivia.objects.create(name='poetry', questions='1', slug='poetry', category_id='2', description='Hi')

      client = APIClient()
      response = client.get('/api/v1/latest-trivias/', format='json')
      response = response.data
      # print(type(response))
      for item in response:
        print(item['get_absolute_url']) 

      # print(response.data)
      # print(response.data[0])

      # serializer = TriviaSerializer(trivias, many = True)
      # data = Response(serializer.data)
      # print(data)