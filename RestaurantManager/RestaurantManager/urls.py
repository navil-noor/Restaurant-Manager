"""
Configurazione URL per il progetto Restaurant Manager.

Tutti gli URL del progetto sono definiti di seguito. Questo è il punto di ingresso
principale di il progetto Restaurant Manager.

"""
from django.contrib import admin

from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant Manager API Documentation",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # configurazione per l'amministratore principale situato su localhost:8000/admin o 127.0.0.1:8000/admin
    path('admin/', admin.site.urls),
    # La funzione include viene utilizzata per aggiungere altri file urls.py, dalla FoodApp
    path('api/', include('FoodApp.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),

    # Redirect for Django Login
    path('accounts/login/', RedirectView.as_view(url=reverse_lazy('admin:login'), permanent=True)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

