from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "description", "release", "rating", "country", "img", "genre"]
        widgets = {
            'release': forms.DateInput(attrs={'type': 'date'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=50)
    text = forms.CharField(max_length=1000) 