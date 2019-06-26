from django import forms
from .models import Components

class ComponentsForm(forms.ModelForm):
    class Meta:
        model = Components
        fields = ('name_type', 'name', 'serial_number', 'country')