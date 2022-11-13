from unicodedata import category
from django.http import Http404, HttpResponseBadRequest

from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

import trivia


from .models import Category, TriviaFavorite, CategoryFavorite, Trivia, Question, Score
from .serializer import TriviaSerializer, CategorySerializer, QuestionSerializer, TriviaFavoriteSerializer, CategoryFavoriteSerializer, ScoreSerializer
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

class TriviaFavoriteDetail(APIView):
  def get_object(self, user_id):
    try:
      return TriviaFavorite.objects.filter(user_id = user_id)
    except Question.DoesNotExist:
      raise Http404
  def get(self, request, user_id, format=None):
    favorites = self.get_object(user_id)
    serializer = TriviaFavoriteSerializer(favorites, many=True)
    return Response(serializer.data)

class AddTriviaFavorite(APIView):
  def add_favorite(self,category_id, trivia_id, user_id):
    try:
      return TriviaFavorite.objects.create( category_id = category_id, trivia_id = trivia_id, user_id = user_id)
    except Question.DoesNotExist:
      raise Http404
  def post(self, request, category_id, trivia_id, user_id, format=None):
    self.add_favorite(category_id, trivia_id, user_id)
    return Response("Added")

class UnaddTriviaFavorite(APIView):
  def unadd_favorite(self,category_id, trivia_id, user_id):
    try:
      query = TriviaFavorite.objects.get( category_id = category_id, trivia_id = trivia_id, user_id = user_id)
      query.delete()
      return Response("Deleted!")
    except Question.DoesNotExist:
      raise Http404
  def post(self, request, category_id, trivia_id, user_id, format=None):
    self.unadd_favorite(category_id, trivia_id, user_id)
    return Response("Added!")

class IsTriviaFavorite(APIView):
  def is_favorite(self,category_id, trivia_id, user_id):
    try:
      query = TriviaFavorite.objects.get( category_id = category_id, trivia_id = trivia_id, user_id = user_id)
      return True
    except:
      return False
  def get(self, request, category_id, trivia_id, user_id, format=None):
    return Response(self.is_favorite(category_id, trivia_id, user_id))

class CategoryDetailViaID(APIView):
  def get_object(self, category_id):
    try:
      return Category.objects.filter(id = category_id)
    except Question.DoesNotExist:
      raise Http404
  def get(self, request, category_id, format=None):
    categries = self.get_object(category_id)
    serializer = CategorySerializer(categries, many=True)
    return Response(serializer.data)


class CategoryFavoriteDetail(APIView):
  def get_object(self, user_id):
    try:
      return CategoryFavorite.objects.filter(user_id = user_id)
    except Question.DoesNotExist:
      raise Http404
  def get(self, request, user_id, format=None):
    favorites = self.get_object(user_id)
    serializer = CategoryFavoriteSerializer(favorites, many=True)
    return Response(serializer.data)

class AddCategoryFavorite(APIView):
  def add_favorite(self,category_id, user_id):
    try:
      return CategoryFavorite.objects.create( category_id = category_id, user_id = user_id)
    except Question.DoesNotExist:
      raise Http404
  def post(self, request, category_id, user_id, format=None):
    self.add_favorite(category_id, user_id)
    return Response("Added")

class UnaddCategoryFavorite(APIView):
  def unadd_favorite(self,category_id, user_id):
    try:
      query = CategoryFavorite.objects.get( category_id = category_id, user_id = user_id)
      query.delete()
      return Response("Deleted!")
    except Question.DoesNotExist:
      raise Http404
  def post(self, request, category_id, user_id, format=None):
    self.unadd_favorite(category_id, user_id)
    return Response("Added!")

class IsCategoryFavorite(APIView):
  def is_favorite(self,category_id, user_id):
    try:
      query = CategoryFavorite.objects.get( category_id = category_id, user_id = user_id)
      return True
    except:
      return False
  def get(self, request, category_id, user_id, format=None):
    return Response(self.is_favorite(category_id, user_id))

class SubmitTrivia(APIView):
  def submit_trivia(self, trivia_slug, user_id, score):
    try:
      trivia_id = Trivia.objects.get(slug=trivia_slug).id
      oldscore = Score.objects.filter(trivia_id = trivia_id, user_id = user_id)
      if oldscore.exists():
        oldscore = oldscore[0]
        oldscore.score = score
        oldscore.save()
        return oldscore
      return Score.objects.create(trivia_id = trivia_id, user_id = user_id, score = score)
    except:
      raise HttpResponseBadRequest
  def post(self, request, trivia_slug, user_id, score, format=None):
    submit = self.submit_trivia(trivia_slug, user_id, score)
    serializer = ScoreSerializer(submit)
    return Response(serializer.data)

class UserTriviaScore(APIView):
  def get_score(self, trivia_slug, user_id):
    try:
      trivia_id = Trivia.objects.get(slug=trivia_slug).id
      return Score.objects.filter(trivia_id = trivia_id, user_id = user_id)
    except:
      return 0
  def get(self, request, trivia_slug, user_id, format=None):
    score = self.get_score(trivia_slug, user_id)
    serializer = ScoreSerializer(score, many=True)
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
    serializer = self.serializer_class(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
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
    trivias = Trivia.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query))
    serializer = TriviaSerializer(trivias, many=True)
    return Response(serializer.data)
  else:
    return Response({"trivias": []})
