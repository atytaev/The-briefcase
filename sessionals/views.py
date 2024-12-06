from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

from films.models import Film
from .models import Sessionals


@login_required
def session_list(request):
    today = now().date()
    sessions = Sessionals.objects.filter(start_time__date__gte=today).order_by('start_time')

    dates = sorted(set(session.start_time.date() for session in sessions))

    selected_date = request.GET.get('date')
    if selected_date:
        sessions = sessions.filter(start_time__date=selected_date)
    else:
        selected_date = today
        sessions = sessions.filter(start_time__date=today)

    films = Film.objects.filter(sessionals__in=sessions).distinct()

    return render(request, 'session_list.html', {
        'dates': dates,
        'selected_date': selected_date,
        'sessions': sessions,
        'films': films,
    })


def session_detail(request, pk):
    session = get_object_or_404(Sessionals, pk=pk)
    return render(request, 'session_detail.html', {'session': session})