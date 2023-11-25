from django.test import TestCase
from .models import Restaurant, Recipe, Ingredient


class RestaurantTestCase(TestCase):
    def setUp(self):
        # Create test data
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        recipe = Recipe.objects.create(name='Test Recipe')
        recipe.ingredients.add(ingredient)
        restaurant = Restaurant.objects.create(name='Test Restaurant')
        restaurant.recipes.add(recipe)

    def test_restaurant_has_recipe(self):
        restaurant = Restaurant.objects.get(name='Test Restaurant')
        self.assertEqual(restaurant.recipes.count(), 1)
