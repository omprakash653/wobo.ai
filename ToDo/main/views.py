from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated  
from rest_framework.views import APIView

# Create your views here.
class ListTodo(generics.ListAPIView):
    
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

class obtain_auth_token(APIView):
    permission_classes = (IsAuthenticated,)