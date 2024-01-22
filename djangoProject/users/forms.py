from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
    PasswordChangeForm,
    PasswordResetForm,
)
from users.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField()
    password = forms.CharField()

    # username = forms.CharField(
    #     label="Имя",
    #     widget=forms.TextInput(
    #         attrs={
    #             "autofocus": True,
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя пользователя",
    #         }
    #     )
    # )
    # password = forms.CharField(
    #     label="Пароль",
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "autocomplete": "current-password",
    #             "class": "form-control",
    #             "placeholder": "Введите ваш пароль",
    #         }
    #     )
    # )


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        ]

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()


class UserChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ["password1", "password2"]

    # password1 = forms.CharField()
    # password2 = forms.CharField()


# class UserPasswordResetForm(PasswordResetForm):
#     class Mete:
#         model = User
#         fields = ["email"]
