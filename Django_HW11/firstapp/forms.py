from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "description", "release", "rating", "country", "img"]
        widgets = {
            'release': forms.DateInput(attrs={'type': 'date'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }
        