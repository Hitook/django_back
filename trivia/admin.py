from django.contrib import admin

from .models import Category, Trivia, Question, User, Favorite
# Register your models here.

admin.site.register(Category)
admin.site.register(Trivia)
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Favorite)
