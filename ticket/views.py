from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from sessionals.models import Sessionals
from .models import Ticket


@login_required
def book_ticket(request, session_id):
    session = get_object_or_404(Sessionals, id=session_id)
    booked_seats = list(Ticket.objects.filter(session=session).values_list('seat_number', flat=True))

    total_seats = session.available_seats

    seat_rows = [list(range(i, min(i + 10, total_seats + 1))) for i in range(1, total_seats + 1, 10)]

    if request.method == 'POST':
        raw_seat_numbers = request.POST.getlist('seat_numbers') or []

        seat_numbers = []
        for raw_seat in raw_seat_numbers:
            seat_numbers.extend(raw_seat.split(','))

        seat_numbers = [int(seat) for seat in seat_numbers if seat and seat.isdigit()]

        if not seat_numbers:
            return render(request, 'book_ticket.html', {
                'session': session,
                'seat_rows': seat_rows,
                'booked_seats': booked_seats,
                'error_message': 'Вы не выбрали ни одного места. Пожалуйста, выберите хотя бы одно место.',
            })

        # Проверяем, не заняты ли места
        for seat_number in seat_numbers:
            if seat_number in booked_seats:
                return render(request, 'book_ticket.html', {
                    'session': session,
                    'seat_rows': seat_rows,
                    'booked_seats': booked_seats,
                })
            print(booked_seats)

        # Создаем билеты для всех выбранных мест
        for seat_number in seat_numbers:
            Ticket.objects.create(
                session=session,
                user=request.user,
                seat_number=seat_number,
            )

        return redirect('ticket_success')
    return render(request, 'book_ticket.html', {
        'session': session,
        'seat_rows': seat_rows,
        'booked_seats': booked_seats,
    })


def ticket_success(request):
    return render(request, 'ticket_success.html')

def cancel_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    session = ticket.session

    session.available_seats += 1
    session.save()

    ticket.delete()

    return redirect('film_list')

@login_required
def user_ticket(request):
    tickets = Ticket.objects.filter(user=request.user).select_related('session')

    for ticket in tickets:
        ticket.payment_status = "Оплачен" if ticket.is_paid else "Не оплачен"

    return render(request, 'user_ticket.html', {
        'tickets': tickets,
    })

# @login_required
# def pay_ticket(request, ticket_id):
#     ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
#
#     if ticket.is_paid:
#         messages.error(request, "Этот билет уже оплачен.")
#         return redirect('my_tickets')
#
#     # Здесь можно добавить реальную оплату через платежный сервис
#
#     # Обновляем статус оплаты
#     ticket.is_paid = True
#     ticket.save()
#
#     messages.success(request, "Вы успешно оплатили билет.")
#     return redirect('my_tickets')

@login_required
def payment_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)

    if ticket.is_paid:
        messages.info(request, "Этот билет уже оплачен.")
        return redirect('user_ticket')

    # Пример суммы для оплаты (можно динамически менять)
    amount = 10

    return render(request, 'payment.html', {'amount': amount})

@login_required
def payment_success(request):
    order_id = request.GET.get('orderID')
    # Реализуйте логику проверки и обновления статуса оплаты
    messages.success(request, "Оплата успешно завершена!")
    return render(request, 'payment_success.html', {'order_id': order_id})

@login_required
def payment_failed(request):
    messages.error(request, "Оплата не удалась. Пожалуйста, попробуйте еще раз.")
    return render(request, 'payment_failed.html')