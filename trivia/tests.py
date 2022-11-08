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
    
     def test_trivia(self):

      Category.objects.create(name='Math', )
      Trivia.objects.create(name='math', questions='1', slug='math', category_id='1', description='less annoying math')
      client = APIClient()
      response = client.get('/api/v1/latest-trivias/', format='json')
      response = response.data
      for item in response:
        print(item) 
        self.assertEqual(item['name'], 'math')
        self.assertEqual(item['id'], 1)
        self.assertEqual(item['description'], 'less annoying math')

      # print(response.data)
      # print(response.data[0])

      # serializer = TriviaSerializer(trivias, many = True)
      # data = Response(serializer.data)
      # print(data)
