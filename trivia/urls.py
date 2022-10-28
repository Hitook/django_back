from django.urls import path, include

from trivia import views


urlpatterns = [
  path('latest-trivias/', views.LatestTriviasList.as_view()),
  path('trivias/display-categories/', views.DisplayCategoriesList.as_view()),
  path('trivias/search/', views.search),
  path('trivias/<slug:category_slug>/<slug:trivia_slug>/', views.TriviaDetail.as_view()),
  path('trivias/<int:trivia_id>/', views.TriviaDetailViaID.as_view()),
  path('trivias/<slug:category_slug>/', views.CategoryDetail.as_view()),
  path('<slug:trivia_slug>/questions', views.QuestionDetail.as_view()),
  path('api-token-auth/', views.CustomAuthToken.as_view()),
  path('user-info/', views.UserInfo.as_view()),
  path('favorites/<int:user_id>/', views.FavoriteDetail.as_view()),
  path('favorite/<int:category_id>/<int:trivia_id>/<int:user_id>/', views.AddFavorite.as_view()),

]