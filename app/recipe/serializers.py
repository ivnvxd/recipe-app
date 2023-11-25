"""
Serializers for recipe APIs
"""

from core.models import Recipe, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Tag
        fields = ("id", "name")
        read_only_fields = ["id"]


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = (
            "id",
            "title",
            "time_minutes",
            "price",
            "link",
            "tags",
        )
        read_only_fields = ["id"]

    def create(self, validated_data):
        """Create a new recipe."""
        tags = validated_data.pop("tags", [])
        recipe = Recipe.objects.create(**validated_data)
        auth_user = self.context["request"].user
        for tag in tags:
            tag_obj, _ = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)

        return recipe


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ("description",)
