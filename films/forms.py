from django import forms
from genres.models import Genre

class FilmFilterForm(forms.Form):
    title = forms.CharField(label='Название', required=False, widget=forms.TextInput(attrs={'placeholder': 'Введите название'}))
    genre = forms.ModelChoiceField(label='Жанр', queryset=Genre.objects.all(), required=False)
    year_min = forms.IntegerField(label='Год (от)', required=False, widget=forms.NumberInput(attrs={'placeholder': 'От'}))
    year_max = forms.IntegerField(label='Год (до)', required=False, widget=forms.NumberInput(attrs={'placeholder': 'До'}))