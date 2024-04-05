from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from user.forms import RegisterForm, LoginForm, ProfileForm
from user.models import Users


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'user/register.html', {'form': form})

        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        age = form.cleaned_data.get('age')
        bio = form.cleaned_data.get('bio')
        avatar = form.cleaned_data.get('avatar')

        Users.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            age=age,
            bio=bio,
            avatar=avatar
        )

        return redirect('/')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', {'form': form})
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)  # User Object or None

        if user is None:
            form.add_error(None, 'Пользователь не найден!')
            return render(request, 'user/login.html', {'form': form})

        login(request, user)

        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/auth/login/')
def profile_view(request):
    return render(request, 'user/profile.html')
def profile_update_view(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
                update_session_auth_hash(request, user)
            user.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'user/profile_update.html', {'form': form})
