from unicodedata import category
from django.http import Http404

from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Category, Trivia
from .serializer import TriviaSerializer, CategorySerializer
# Create your views here.

class LatestTriviasList(APIView):
  def get(self, request, format=None):
    trivias = Trivia.objects.all()[0:4]
    serializer = TriviaSerializer(trivias, many=True)
    return Response(serializer.data)

class LatestCategoriesList(APIView):
  def get(self, request, format=None):
    categories = Category.objects.all()[0:4]
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

class TriviaDetail(APIView):
  def get_object(self, category_slug, trivia_slug):
    try:
      return Trivia.objects.filter(category__slug=category_slug).get(slug=trivia_slug)
    except Trivia.DoesNotExist:
      raise Http404
  def get(self, request, category_slug, trivia_slug, format=None):
    trivia = self.get_object(category_slug, trivia_slug)
    serializer = TriviaSerializer(trivia)
    return Response(serializer.data)
class CategoryDetail(APIView):
  def get_object(self, category_slug):
    try:
      return Category.objects.get(slug=category_slug)
    except Category.DoesNotExist:
      raise Http404
  def get(self, request, category_slug, format=None):
    category = self.get_object(category_slug)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['POST'])
def search(request):
  query = request.data.get('query', '')
  
  if query:
    trivias = Trivia.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    serializer = TriviaSerializer(trivias, many=True)
    return Response(serializer.data)
  else:
    return Response({"trivias": []})
