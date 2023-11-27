# Test unitari per verificare che i modelli si comportino come previsto e gestiscano
# tutti i casi in modo appropriato
from django.test import TestCase
from .models import Ingredient, Recipe, Restaurant


class ModelsTestCase(TestCase):
    def test_create_ingredient(self):
        # Prova a creare un ingrediente
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        self.assertEqual(ingredient.name, 'Test Ingredient')

    def test_create_recipe_with_ingredient(self):
        # Prova a creare una ricetta con un ingrediente
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        recipe = Recipe.objects.create(name='Test Recipe')
        recipe.ingredients.add(ingredient)
        self.assertEqual(recipe.ingredients.count(), 1)

    def test_create_restaurant_with_recipe(self):
        # Prova a creare un ristorante con una ricetta
        ingredient = Ingredient.objects.create(name='Test Ingredient')
        recipe = Recipe.objects.create(name='Test Recipe')
        recipe.ingredients.add(ingredient)
        restaurant = Restaurant.objects.create(name='Test Restaurant')
        restaurant.recipes.add(recipe)
        self.assertEqual(restaurant.recipes.count(), 1)

    def test_create_ingredient_without_name(self):
        # Ingrediente senza nome (test fallito)
        with self.assertRaises(ValueError):
            Ingredient.objects.create(name='')

    def test_create_recipe_without_name(self):
        # Ricetta senza nome (test fallito)
        with self.assertRaises(ValueError):
            Recipe.objects.create(name='')

    def test_create_restaurant_without_name(self):
        # Ristorante senza nome (test fallito) (should fail)
        with self.assertRaises(ValueError):
            Restaurant.objects.create(name='')
