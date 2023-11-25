from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient)


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    recipes = models.ManyToManyField(Recipe)
