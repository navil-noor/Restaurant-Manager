# I modelli di dati vengono creati in questo file. Qui è dove definire le operazioni CRUD
# per le entità.
from django.db import models


# Modello di ingredienti che possono essere utilizzati nelle ricette. Ha solo il nome,
# altri attributi possono essere aggiunti come la quantità.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Modello di ricetta che può essere composto da più ingredienti (ManyToManyField).
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    def __str__(self):
        return self.name


# Modello di ristorante che può avere più ricette (ManyToManyField).
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    recipes = models.ManyToManyField(Recipe, related_name='restaurants')

    def __str__(self):
        return self.name
