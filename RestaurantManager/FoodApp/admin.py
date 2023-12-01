from django.contrib import admin
from .models import Ingredient, Recipe, Restaurant


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_ingredients', 'display_restaurants')
    list_filter = ('ingredients', 'restaurants')

    def display_ingredients(self, obj):
        return ", ".join(set([ingredient.name for ingredient in obj.ingredients.all()]))

    display_ingredients.short_description = 'Ingredients'

    def display_restaurants(self, obj):
        return ", ".join(set([restaurant.name for restaurant in obj.restaurants.all()]))

    display_restaurants.short_description = 'Restaurants'


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_recipes')
    list_filter = ('recipes',)

    def display_recipes(self, obj):
        return ", ".join(set([recipe.name for recipe in obj.recipes.all()]))

    display_recipes.short_description = 'Recipes'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_recipes', 'display_restaurants')
    list_filter = ('recipes', 'recipes__restaurants')  # Use the actual fields with __ notation

    def display_recipes(self, obj):
        return ", ".join(set([recipe.name for recipe in obj.recipes.all()]))

    display_recipes.short_description = 'Recipes'

    def display_restaurants(self, obj):
        return ", ".join(set([restaurant.name for recipe in obj.recipes.all() for restaurant in recipe.restaurants.all()]))

    display_restaurants.short_description = 'Restaurants'
