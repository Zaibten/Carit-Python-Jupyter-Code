# predictor/forms.py

from django import forms

class PredictionForm(forms.Form):
    FUEL_TYPE_CHOICES = [
        (0, 'Petrol'),
        (1, 'Diesel'),
        (2, 'Hybrid'),
        (3, 'Electric'),
        (4, 'LPG'),
    ]
    
    SELLER_TYPE_CHOICES = [
        (0, 'Customer'),
        (1, 'PakWheels'),
    ]
    
    TRANSMISSION_CHOICES = [
        (0, 'Manual'),
        (1, 'Automatic'),
    ]

    present_price = forms.FloatField(label='Purchase Price')
    kms_driven = forms.FloatField(label='Kms Driven')
    fuel_type = forms.ChoiceField(label='Fuel Type', choices=FUEL_TYPE_CHOICES, widget=forms.RadioSelect)
    seller_type = forms.ChoiceField(label='Seller Type', choices=SELLER_TYPE_CHOICES, widget=forms.RadioSelect)
    transmission = forms.ChoiceField(label='Transmission', choices=TRANSMISSION_CHOICES, widget=forms.RadioSelect)
    age = forms.FloatField(label='Car Age')
