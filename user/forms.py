from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        min_length=3,
        required=True,
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин'
            }
        )
    )
    password = forms.CharField(
        max_length=150,
        min_length=8,
        required=True,
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }
        )
    )
    password2 = forms.CharField(
        max_length=150,
        min_length=8,
        required=True,
        label='Повторите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }
        )
    )
    first_name = forms.CharField(
        max_length=150,
        required=False,
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }
        )
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }
        )
    )
    age = forms.IntegerField(
        required=False,
        label='Возраст',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите возраст'
            }
        )
    )
    bio = forms.CharField(
        required=False,
        label='О себе',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Расскажите о себе'
            }
        )
    )
    avatar = forms.ImageField(
        required=False,
        label='Аватар',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control-file'
            }
        )
    )

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Пароли не совпадают!')

        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        min_length=3,
        required=True,
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин'
            }
        )
    )
    password = forms.CharField(
        max_length=150,
        min_length=8,
        required=True,
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }
        )
    )