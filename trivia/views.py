from unicodedata import category
from django.http import Http404

from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

import trivia


from .models import Category, Favorite, Trivia, Question
from .serializer import TriviaSerializer, CategorySerializer, QuestionSerializer, FavoriteSerializer
from trivia import serializer
# Create your views here.

class LatestTriviasList(APIView):
  def get(self, request, format=None):
    trivias = Trivia.objects.all()[0:4]
    serializer = TriviaSerializer(trivias, many=True)
    return Response(serializer.data)

class DisplayCategoriesList(APIView):
  def get(self, request, format=None):
    categories = Category.objects.all()
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
  def get_questions(self, request, category_slug, trivia_slug):
    trivia = self.get_object(category_slug, trivia_slug)
    questions = Question.objects.filter(trivia_id = trivia.id)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

class TriviaDetailViaID(APIView):
  def get_object(self, trivia_id):
    try:
      return Trivia.objects.filter(id = trivia_id)
    except Question.DoesNotExist:
      raise Http404
  def get(self, request, trivia_id, format=None):
    trivias = self.get_object(trivia_id)
    serializer = TriviaSerializer(trivias, many=True)
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

class QuestionDetail(APIView):
  def get_object(self, trivia_slug):
    try:
      return Question.objects.filter(trivia_id = Trivia.objects.get(slug=trivia_slug).id)
    except Question.DoesNotExist:
      raise Http404
  def get(self, request, trivia_slug, format=None):
    question = self.get_object(trivia_slug)
    serializer = QuestionSerializer(question, many=True)
    return Response(serializer.data)

class FavoriteDetail(APIView):
  def get_object(self, user_id):
    try:
      return Favorite.objects.filter(user_id = user_id)
    except Question.DoesNotExist:
      raise Http404
  def get(self, request, user_id, format=None):
    favorites = self.get_object(user_id)
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)

class FavoriteList(APIView):
  def get(self, request, format=None):
    favorites = Favorite.objects.all()
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class UserInfo(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print(user.username)
        return Response({
          'username' : user.username,
          'user_id': user.pk,
          'email': user.email
        })

@api_view(['POST'])
def search(request):
  query = request.data.get('query', '')
  # Implement searching by category
  if query:
    trivias = Trivia.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    serializer = TriviaSerializer(trivias, many=True)
    return Response(serializer.data)
  else:
    return Response({"trivias": []})
