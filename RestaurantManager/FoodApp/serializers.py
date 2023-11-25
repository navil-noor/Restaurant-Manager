from rest_framework import serializers
from .models import Restaurant, Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
