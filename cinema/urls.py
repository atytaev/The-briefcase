from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from films.views import film_list, film_detail
from sessionals.views import session_list, session_detail
from ticket.views import ticket_success, book_ticket, cancel_ticket
from users.views import register, user_login, user_logout
from actors.views import actor_detail
from directors.views import director_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    #films
    path('', film_list, name='film_list'),
    path('film/<int:pk>/', film_detail, name='film_detail'),
    #sessionals
    path('session/', session_list, name='session_list'),
    path('session/<int:pk>/', session_detail, name='session_detail'),
    #ticket
    path('book/<int:session_id>/', book_ticket, name='book_ticket'),
    path('success/', ticket_success, name='ticket_success'),
    path('book/<int:session_id>/cancel_ticket', cancel_ticket, name='cancel_ticket'),
    #users
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    #actor & directors
    path('actor/<int:pk>/', actor_detail, name='actor_detail'),
    path('director/<int:pk>/', director_detail, name='director_detail'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)