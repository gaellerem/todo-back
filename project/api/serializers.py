from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=100,
        error_messages={
            "unique": "Cette catégorie existe déjà !",
            "blank": "Le nom de la catégorie ne peut pas être vide."
        }
    )
    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = ["id"]

    def validate_name(self, value):
        if Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError("Cette catégorie existe déjà !")
        return value


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

    def validate_category(self, value):
        if not Category.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Cette catégorie n'existe pas.")
        return value