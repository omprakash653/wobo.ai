from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view()),
    path('main-token-auth/', obtain_auth_token, name='main_token_auth'),
]