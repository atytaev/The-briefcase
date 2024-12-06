from django.db import models
from users.models import User
from sessionals.models import Sessionals

class Ticket(models.Model):
    session = models.ForeignKey(Sessionals, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    seat_number = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Ticket for {self.session.film.title} ({self.seat_number})"

    def delete(self, *args, **kwargs):
        self.session.available_seats += 1
        self.session.save()

        # Теперь можно удалять сам билет
        super(Ticket, self).delete(*args, **kwargs)