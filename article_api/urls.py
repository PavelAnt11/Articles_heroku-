from django.urls import path
from .views import *


urlpatterns = [
    path('list_articles/', ArticlesAPIList.as_view()),
    path('add_article/', ArticleAPICreate.as_view()),
    path('update_article/<int:pk>/', ArticleAPIUpdate.as_view()),
    path('delete_article/<int:pk>/', ArticleAPIDelete.as_view()),
    path('register/', CreateUserView.as_view()),
    path('logout/', Logout.as_view()),
]
