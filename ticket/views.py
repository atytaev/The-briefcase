from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from sessionals.models import Sessionals
from django.contrib.auth.decorators import login_required

@login_required
def book_ticket(request, session_id):
    session = get_object_or_404(Sessionals, id=session_id)

    # Получаем все занятые места
    booked_seats = list(Ticket.objects.filter(session=session).values_list('seat_number', flat=True))

    # Всего мест в зале
    total_seats = session.available_seats

    # Разбиваем все места (1..total_seats) на ряды по 10
    seat_rows = [list(range(i, min(i + 10, total_seats + 1))) for i in range(1, total_seats + 1, 10)]

    if request.method == 'POST':
        seat_number = int(request.POST.get('seat_number'))

        # Проверяем, занято ли место
        if seat_number in booked_seats:
            return render(request, 'book_ticket.html', {
                'session': session,
                'seat_rows': seat_rows,
                'booked_seats': booked_seats,
                'error_message': 'Это место уже забронировано. Пожалуйста, выберите другое место.',
            })

        # Бронируем место
        Ticket.objects.create(
            session=session,
            user=request.user,
            seat_number=seat_number,
        )
        session.available_seats -= 1  # Уменьшаем общее количество доступных мест
        session.save()

        return redirect('ticket_success')  # Перенаправляем на страницу успеха

    return render(request, 'book_ticket.html', {
        'session': session,
        'seat_rows': seat_rows,
        'booked_seats': booked_seats,
    })


def ticket_success(request):
    return render(request, 'ticket_success.html')

def cancel_ticket(request, ticket_id):
    # Получаем билет по ID
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    # Получаем сеанс, связанный с этим билетом
    session = ticket.session

    # Увеличиваем количество доступных мест на 1
    session.available_seats += 1
    session.save()

    # Удаляем билет
    ticket.delete()

    # Перенаправляем на страницу успешного отказа от билета
    return redirect('film_list')  # Укажите нужный URL