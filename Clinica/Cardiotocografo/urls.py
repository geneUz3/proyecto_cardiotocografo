from django.urls import path, include
from .views import PersonaCreate, registrada


urlpatterns = [
    path('persona_registrada', registrada, name = 'cardiotocografo'),
    path('', PersonaCreate.as_view(), name = 'guardar_persona'),
]