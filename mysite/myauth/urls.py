from django.urls import path
from .views import login_view

app_name = "myauth"

urlpatterns = [
    path("", login_view, name="login"),  # Главная страница приложения
    path("login/", login_view, name="login"),  # Страница логина
]
