from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('test-railway/', views.railway_test, name='railway_test'),
]