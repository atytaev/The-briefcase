from django.shortcuts import render, get_object_or_404

from .models import Film
from .forms import FilmFilterForm

def film_list(request):
    films = Film.objects.all()
    form = FilmFilterForm(request.GET)

    if form.is_valid():
        title = form.cleaned_data.get('title')
        genre = form.cleaned_data.get('genre')
        year_min = form.cleaned_data.get('year_min')
        year_max = form.cleaned_data.get('year_max')

        if title:
            films = films.filter(title__icontains=title)
        if genre:
            films = films.filter(genre=genre)
        if year_min:
            films = films.filter(year__gte=year_min)
        if year_max:
            films = films.filter(year__lte=year_max)

    return render(request, 'film_list.html', {'films': films, 'form': form})



def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'films_detail.html', {'film': film})
