# predictor/views.py

import os
from django.conf import settings
import pandas as pd
import joblib
from django.shortcuts import render

#from car_price_prediction.car_price_prediction import settings
from .forms import PredictionForm

# predictor/views.py

from django.shortcuts import redirect

def redirect_to_predict(request):
    return redirect('predict_price')  # Redirect to the predict_price URL



def predict_price(request):
    result = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get input values from the form
            p1 = form.cleaned_data['present_price']  # Present_Price
            p2 = form.cleaned_data['kms_driven']      # Kms_Driven
            p3 = form.cleaned_data['fuel_type']       # Fuel_Type (0-4)
            p4 = form.cleaned_data['seller_type']     # Seller_Type (0-1)
            p5 = form.cleaned_data['transmission']     # Transmission (0-1)
            p6 = form.cleaned_data['age']              # Age
            
            # Load the pre-trained model with the correct path
            model_path = 'C:/Users/lenovo/Desktop/Car Biding & Verifiation Project/Web Application/Web App/Extra/car_price_prediction/predictor/car_price_predictor'
            model = joblib.load(model_path)
            
            # Create a DataFrame with the input values and set appropriate dtypes
            data_new = pd.DataFrame({
                'Present_Price': [p1],
                'Kms_Driven': [p2],
                'Fuel_Type': [int(p3)],          # Convert to integer
                'Seller_Type': [int(p4)],        # Convert to integer
                'Transmission': [int(p5)],       # Convert to integer
                'Age': [p6]
            })
            
            # Ensure the data types are correct
            data_new['Present_Price'] = data_new['Present_Price'].astype(float)
            data_new['Kms_Driven'] = data_new['Kms_Driven'].astype(float)
            data_new['Age'] = data_new['Age'].astype(float)
            
            # Predict the price
            result = model.predict(data_new)
    else:
        form = PredictionForm()

    return render(request, 'predict.html', {'form': form, 'result': result})