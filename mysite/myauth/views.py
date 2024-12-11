from http.client import HTTPResponse

from django.contrib.auth.views import LogoutView
from django.contrib.sessions.models import Session
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy


def login_view(request: HttpRequest) -> HTTPResponse:
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request, 'myauth/login.html')

    # Обрабатываем POST-запрос
    username = request.POST.get("username")
    password = request.POST.get("password")

    if not username or not password:
        return render(request, "myauth/login.html", {"error": "Username and password are required."})

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/admin/")

    return render(request, "myauth/login.html", {"error": "Invalid login credentials"})

def logout_view(request:HttpRequest):
    logout(request)
    return redirect(reverse("myauth:login"))

class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("fizz", "buzz", max_age=3600)  # Кука "fizz" установлена на 1 час
    return response

def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("fizz", "default value")
    return HttpResponse(f"Cookie value: {value!r}")

from django.http import HttpRequest, HttpResponse

def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameeggs"  # Устанавливаем значение сессии
    return HttpResponse("Session set!")

def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foobar", "default")  # Получаем значение из сессии
    return HttpResponse(f"Session value: {value!r}")
