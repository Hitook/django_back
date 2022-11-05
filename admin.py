from django.contrib import admin

from .models import Category, Trivia, Question, User, Favorite
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Trivia)
class TriviaAdmin(admin.ModelAdmin):
    pass
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass
