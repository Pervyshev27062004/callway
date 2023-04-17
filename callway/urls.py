from django.contrib import admin
from django.urls import path
from users.views import login_view, register
from products.views import index

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('login_view/', login_view, name="login_view"),
    path('register/', register, name="register"),
]
