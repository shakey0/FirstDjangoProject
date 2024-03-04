from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ProfilePictureForm


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. Welcome!')
            return redirect('login')
    return render(request, 'register.html', {'form': form})


def login(request):
    form = LoginForm(request.POST or None)
    next_url = request.POST.get('next') or request.GET.get('next', 'food:index')
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password')
    return render(request, 'login.html', {'form': form, 'next': next_url})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('food:index')


@login_required
def user_profile(request):
    form = ProfilePictureForm()
    return render(request, 'user-profile.html', {'form': form})


@login_required
def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.image = form.cleaned_data.get('profile_picture')
            request.user.profile.save()
            messages.success(request, 'Profile picture uploaded successfully')
            return redirect('profile')
