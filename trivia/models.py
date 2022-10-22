from email.policy import default
from pydoc import describe
from tkinter import Image
from io import BytesIO
from unicodedata import category, decimal
from unittest.util import _MAX_LENGTH
from PIL import Image

from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
# Create your models here.
class Account(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
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

class Favorite(models.Model):
  trivia = models.ForeignKey(Trivia, related_name='favorite', on_delete=models.CASCADE)
  category = models.ForeignKey(Category, related_name='favorite', on_delete=models.CASCADE)
  user = models.ForeignKey(Account, related_name='account', on_delete=models.CASCADE)

  def __str__(self):
    return self.question

