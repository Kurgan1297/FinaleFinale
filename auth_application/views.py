from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate as auth_authenticate, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('greetings_page')
    else:
        form = UserCreationForm()

    return render(request, 'auth_application/account_register.html', {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            print("1")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth_authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("greetings_page")
    else:
        form = AuthenticationForm()

    return render(request, 'auth_application/account_login.html', {"form": form})



def logout(request):
    auth_logout(request)

    return redirect("register_page")