# predictor/urls.py

from django.urls import path
from .views import predict_price, redirect_to_predict

urlpatterns = [
    path('', redirect_to_predict, name='redirect_to_predict'),  # Redirect root URL to predict
    path('predict/', predict_price, name='predict_price'),      # Actual prediction view
]
