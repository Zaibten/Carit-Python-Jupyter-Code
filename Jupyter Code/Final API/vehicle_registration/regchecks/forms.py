from django import forms

class VehicleCheckForm(forms.Form):
    registration_number = forms.CharField(label="Vehicle Registration Number", max_length=20)
