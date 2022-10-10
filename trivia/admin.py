from django.contrib import admin

from .models import Category, Trivia, Question
# Register your models here.

admin.site.register(Category)
admin.site.register(Trivia)
admin.site.register(Question)
