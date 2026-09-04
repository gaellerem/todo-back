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

def health_check(request):
    """Une vue simple qui renvoie un statut de succès."""
    return JsonResponse({"status": "ok", "message": "API is healthy"})

def trigger_error(request):
    """Une vue conçue pour créer une erreur 500."""
    # Cette ligne va inévitablement provoquer une erreur
    division_by_zero = 1 / 0
    return JsonResponse({"this": "will never be returned"})