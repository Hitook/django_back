from django.urls import path, include

from trivia import views


urlpatterns = [
  path('latest-trivias/', views.LatestTriviasList.as_view()),
  path('trivias/display-categories/', views.DisplayCategoriesList.as_view()),
  path('trivias/search/', views.search),
  path('trivias/submit/', views.SubmitTrivia.as_view()),
  path('trivias/<slug:category_slug>/<slug:trivia_slug>/', views.TriviaDetail.as_view()),
  path('trivias/<int:trivia_id>/', views.TriviaDetailViaID.as_view()),
  path('trivias/<slug:category_slug>/', views.CategoryDetail.as_view()),
  path('<slug:trivia_slug>/questions', views.QuestionDetail.as_view()),
  path('api-token-auth/', views.CustomAuthToken.as_view()),
  path('user-info/', views.UserInfo.as_view()),
  path('trivia/favorites/<int:user_id>/', views.TriviaFavoriteDetail.as_view()),
  path('trivia/favorite/<int:category_id>/<int:trivia_id>/<int:user_id>/', views.AddTriviaFavorite.as_view()),
  path('trivia/defavorite/<int:category_id>/<int:trivia_id>/<int:user_id>/', views.UnaddTriviaFavorite.as_view()),
  path('trivia/isfavorite/<int:category_id>/<int:trivia_id>/<int:user_id>/', views.IsTriviaFavorite.as_view()),
  path('category/<int:category_id>/', views.CategoryDetailViaID.as_view()),
  path('categories/favorites/<int:user_id>/', views.CategoryFavoriteDetail.as_view()),
  path('category/favorite/<int:category_id>/<int:user_id>/', views.AddCategoryFavorite.as_view()),
  path('category/defavorite/<int:category_id>/<int:user_id>/', views.UnaddCategoryFavorite.as_view()),
  path('category/isfavorite/<int:category_id>/<int:user_id>/', views.IsCategoryFavorite.as_view()),
  path('score/<slug:trivia_slug>/<int:user_id>/', views.UserTriviaScore.as_view()),
  path('trivia/<slug:trivia_slug>/<int:user_id>/<int:score>/', views.SubmitTrivia.as_view()),


]