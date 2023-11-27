# Definire i pattern URL per l'app. Per mappare gli URL alle viste, specificando quale
# vista deve gestire un particolare modello URL. Luogo in cui definire gli endpoint per le app
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, RecipeViewSet, RestaurantViewSet


router = DefaultRouter()  # Router instance
router.register('ingredients', IngredientViewSet)  # registrare i viewset con il router
router.register('recipes', RecipeViewSet)
router.register('restaurants', RestaurantViewSet)

# Definisci i modelli URL dell'API e includi quelli generati dal router
urlpatterns = [
    path('', include(router.urls)),
]

# Per semplificare la creazione di endpoint API RESTful per i modelli nell'app del progetto.
