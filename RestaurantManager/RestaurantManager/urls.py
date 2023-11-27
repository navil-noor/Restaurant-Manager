"""
Configurazione URL per il progetto Restaurant Manager.

Tutti gli URL del progetto sono definiti di seguito. Questo è il punto di ingresso
principale di il progetto Restaurant Manager.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # configurazione per l'amministratore principale situato su localhost:8000/admin o 127.0.0.1:8000/admin
    path('admin/', admin.site.urls),
    # La funzione include viene utilizzata per aggiungere altri file urls.py, dalla FoodApp
    path('api/', include('FoodApp.urls')),
]

