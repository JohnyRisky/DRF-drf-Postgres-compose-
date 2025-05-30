from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLogin(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким e-mail уже существует")
        return email