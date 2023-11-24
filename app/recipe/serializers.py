"""
Serializers for recipe APIs
"""

from core.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "time_minutes",
            "price",
            "link",
        )
        read_only_fields = ["id"]


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ("description",)
