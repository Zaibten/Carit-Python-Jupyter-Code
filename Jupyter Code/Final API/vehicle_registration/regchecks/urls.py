from django.urls import path
from .views import check_vehicle

urlpatterns = [
    path('check-vehicle/', check_vehicle, name='check_vehicle'),  # Only keep the one you want to use
]
