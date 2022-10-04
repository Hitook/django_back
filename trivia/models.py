from email.policy import default
from pydoc import describe
from tkinter import Image
from io import BytesIO
from unicodedata import category, decimal
from PIL import Image

from django.db import models
from django.core.files import File
# Create your models here.

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
  questions = models.IntegerField(null=True)
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