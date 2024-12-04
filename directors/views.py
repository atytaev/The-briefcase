from django.shortcuts import get_object_or_404, render
from .models import Director

def director_detail(request, pk):
    director = get_object_or_404(Director, pk=pk)
    return render(request, 'director_detail.html', {'director': director})

