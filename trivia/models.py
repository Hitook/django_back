from email.policy import default
from pydoc import describe
from tkinter import Image
from io import BytesIO
from unicodedata import category, decimal
from unittest.util import _MAX_LENGTH
# from PIL import Image

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import File
# Create your models here.
class User(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-date_added',)

  def __unicode__(self):
    return self.user.get_full_name()

class Category(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField()

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/{self.slug}/'

class Trivia(models.Model):
  category = models.ForeignKey(Category, related_name='trivias', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  questions = models.IntegerField(default=2)
  average_score = models.IntegerField(default= 0)
  slug = models.SlugField()
  description = models.TextField(blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-date_added',)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return f'/{self.category.slug}/{self.slug}/'
  
class Question(models.Model):
  trivia = models.ForeignKey(Trivia, related_name='question', on_delete=models.CASCADE)
  question = models.CharField(max_length=255)
  correct_answer = models.CharField(max_length=50)
  fake_answer = models.CharField(max_length=50)
  class Meta:
    ordering = ('id',)

  def __str__(self):
    return self.question

class TriviaFavorite(models.Model):
  trivia = models.ForeignKey(Trivia, related_name='favorite', on_delete=models.CASCADE)
  category = models.ForeignKey(Category, related_name='favorite', on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='favorite', on_delete=models.CASCADE)

  class Meta:
      ordering = ('id',)

  def __str__(self):
    return str(self.trivia.name)

class CategoryFavorite(models.Model):
  category = models.ForeignKey(Category, related_name='category_favorite', on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='category_favorite', on_delete=models.CASCADE)
  class Meta:
      ordering = ('id',)

  def __str__(self):
    return str(self.category.name)

class Score(models.Model):
  trivia = models.ForeignKey(Trivia, related_name='score', on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='score', on_delete=models.CASCADE)
  score = models.IntegerField(default= 0)

  class Meta:
      ordering = ('id',)

  def __str__(self):
    return str(self.trivia.name)

