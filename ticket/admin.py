from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'seat_number', 'booked_at')
    search_fields = ('user__username', 'session__film__title', 'seat_number')
    list_filter = ('booked_at', 'session__film', 'user')
    ordering = ('-booked_at',)

    def seat_number(self, obj):
        return f"Seat {obj.seat_number}"

    seat_number.short_description = 'Seat Number'