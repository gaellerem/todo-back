from rest_framework import serializers
from .models import Category, Task
from rest_framework.validators import UniqueValidator


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=100,
        validators=[
            UniqueValidator(
                queryset=Category.objects.all(),
                message="Cette catégorie existe déjà !",
                lookup="iexact"
            )
        ],
        error_messages={
            "blank": "Le nom de la catégorie ne peut pas être vide."
        }
    )
    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = ["id"]

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
        error_messages={
            "does_not_exist": "Cette catégorie n'existe pas.",
            "required": "Vous devez choisir une catégorie."
        }
    )

    class Meta:
        model = Task
        fields = [
            "id",
            "description",
            "is_completed",
            "created_at",
            "category",
            "category_id",
        ]
        read_only_fields = ["id", "created_at", "category"]