# Serializers vengono utilizzati per facilitare la conversione di tipi di dati complessi
# in tipi di dati nativi Python e anche per fare il contrario.
# Lo scopo è rappresentare le relazioni tra modelli in un formato strutturato e serializzato
from rest_framework import serializers
from .models import Restaurant, Recipe, Ingredient


# Qui ModelSerializer viene utilizzato per serializzare e deserializzare le istanze del modello Ingredient.
# I metadati riguardano il processo di serializzazione, creiamo la classe Meta all'interno del serializzatore.
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


# Lo stesso che abbiamo fatto con Ingredient.
class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'


# Lo stesso che abbiamo fatto con Ingredient e Recipe.
class RestaurantSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
