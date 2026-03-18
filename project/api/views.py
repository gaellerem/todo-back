from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer

class CategoryListCreateView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    """
        Vue pour gérer la liste et la création des catégories.
    """
    def perform_create(self, serializer):
        serializer.save()

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    """
        Vue pour gérer la récupération, la mise à jour et la suppression d'une catégorie spécifique.
    """
    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class TaskListCreateView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    """
        Vue pour gérer la liste et la création des tâches.
    """
    def perform_create(self, serializer):
        serializer.save()


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    """
        Vue pour gérer la récupération, la mise à jour et la suppression d'une tâche spécifique.
    """
    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
