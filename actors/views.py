from django.shortcuts import render, get_object_or_404
from .models import Actor
def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, 'actor_detail.html', {'actor': actor})
