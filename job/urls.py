from django.contrib import admin
from django.urls import path
from user.views import login_view, logout_view, register_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', register_view, name='registration'),
]
