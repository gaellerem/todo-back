from django.db import models


class Category(models.Model):
    """
        Modèle pour représenter une catégorie dans l'application.
    """
    name = models.CharField(max_length=100, unique=True)


class Task(models.Model):
    """
        Modèle pour représenter une tâche dans l'application.
    """
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='tasks')