from django.contrib import admin

from .models import Category, Trivia, Question, User, TriviaFavorite, Score
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
@admin.register(TriviaFavorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass

