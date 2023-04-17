from django.contrib import admin
from django.urls import path
from users.views import login_view, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_view/', login_view, name="login_view"),
    path('register/', register, name="register"),
]
