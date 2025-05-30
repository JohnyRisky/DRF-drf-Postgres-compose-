from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserLogin
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login


class TokenLoginView(View):
    template_name = "users/login.html"

    def get(self, request):
        form = UserLogin()
        return render(request, self.template_name, {"title": "Авторизация", "form": form})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if not user:
            return render(request, self.template_name, {
                "title": "Авторизация",
                "form": UserLogin(request.POST),
                "error": "Неверный логин или пароль",
            })

        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        request.session["auth_token"] = token.key

        return redirect("index")
  

class UsersRegistration(CreateView):
    form_class = UserRegistrationForm
    template_name = "users/register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("auth:login")