from django.urls import path, include

from trivia import views


urlpatterns = [
  path('latest-trivias/', views.LatestTriviasList.as_view()),
  path('trivias/latest-categories/', views.LatestCategoriesList.as_view()),
  path('trivias/search/', views.search),
  path('trivias/<slug:category_slug>/<slug:trivia_slug>/', views.TriviaDetail.as_view()),
  path('trivias/<slug:category_slug>/', views.CategoryDetail.as_view()),
]