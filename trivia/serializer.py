from rest_framework import serializers
from .models import Category, Trivia, Question, User, Favorite


class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = (
      "id",
      "question",
      "correct_answer",
      "fake_answer",
      "trivia",
    )
  
class TriviaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Trivia
    fields = (
      "id",
      "category_id",
      "name",
      "get_absolute_url",
      "description",
      "questions",
      "average_score"
    )

class CategorySerializer(serializers.ModelSerializer):
  trivias = TriviaSerializer(many=True)
  class Meta:
    model = Category
    fields = (
      "id",
      "name",
      "get_absolute_url",
      "trivias",
    )

class FavoriteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Favorite
    fields = (
      "id",
      "user_id",
      "trivia_id",
      "category_id",
    )
