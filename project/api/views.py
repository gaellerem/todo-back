from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer

class CategoryListCreateView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TaskListCreateView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

def railway_test(request):
    """Une vue simple pour valider le déploiement sur Railway."""
    return JsonResponse({"message": "API déployée avec succès sur Railway !"})
