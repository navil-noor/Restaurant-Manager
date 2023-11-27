# I viewset possono essere utilizzati in combinazione con i router per generare modelli
# URL per l'API, ciò consente di eseguire operazioni CRUD sui dati.
from rest_framework import viewsets
from .models import Restaurant, Recipe, Ingredient
from .serializers import RestaurantSerializer, RecipeSerializer, IngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()  # l'insieme degli oggetti da utilizzare
    serializer_class = IngredientSerializer  # per convertire le istanze del modello all'interno dei tipi di dati.


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
