from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("order", views.order, name="order"),
    path("change_order", views.change_order, name="change_order"),
    path("show_order", views.show_order, name="show_order")
]
