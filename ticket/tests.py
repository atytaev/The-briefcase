from django.test import TestCase
from django.urls import reverse
from users.models import User
from datetime import date
from films.models import Film
from sessionals.models import Sessionals
from ticket.models import Ticket
from datetime import timedelta
from django.utils import timezone
from datetime import datetime
class TicketBookingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

        self.film = Film.objects.create(
            title='Inception',
            description='A mind-bending thriller',
            release_date=date(2010, 7, 16),
            duration=timedelta(hours=2, minutes=28)
        )

        start_time = timezone.make_aware(datetime(2024, 12, 15, 18, 0))

        self.session = Sessionals.objects.create(film=self.film, available_seats=30, start_time=start_time)
        self.client.login(username='testuser', password='password123')

    def test_book_ticket_success(self):

        response = self.client.post(reverse('book_ticket', args=[self.session.id]), {'seat_numbers': ['1']})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('ticket_success'))

        ticket = Ticket.objects.filter(session=self.session, user=self.user, seat_number=1).exists()
        self.assertTrue(ticket)

    def test_book_ticket_seat_already_booked(self):
        Ticket.objects.create(session=self.session, user=self.user, seat_number=1)
        response = self.client.post(reverse('book_ticket', args=[self.session.id]), {'seat_number': ['1']})

        self.assertEqual(response.status_code, 200)



    def test_book_ticket_no_login(self):
        self.client.logout()

        response = self.client.post(reverse('book_ticket', args=[self.session.id]), {'seat_number': ['1']})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'{reverse("user_login")}?next={reverse("book_ticket", args=[self.session.id])}')