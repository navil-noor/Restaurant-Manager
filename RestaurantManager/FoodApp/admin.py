from django.contrib import admin
from .models import Restaurant, Recipe, Ingredient


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    filter_horizontal = ('ingredients',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


# Register your models with the custom admin classes
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
