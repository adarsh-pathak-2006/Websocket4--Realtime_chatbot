from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from core.forms import AuthForm
from django.contrib.auth import login, authenticate


class RegisterView(View):
    def get(self, request):
        form=AuthForm()
        return render(request, 'register.html', { 'form':form })
    
    def post(self, request):
        form_data=AuthForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            pass1=form_data.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'form':form_data, 'user_err':'username already exists..try another'})
            else:
                user=User.objects.create_user(username=username, password=pass1)
                login(request, user)
                return redirect('login')
        else:
            return render(request, 'login.html', { 'invalid':'invalid inputs' }) 

class LoginView(View):
    def get(self, request):
        form=AuthForm()
        return render(request, 'login.html', { 'form':form })
    
    def post(self, request):
        form_data=AuthForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            password=form_data.cleaned_data['password']
            user=authenticate(username=username, password=password)
            if user is None:
                return render(request, 'login.html', {'user_err':'user does not exist..try registration first'})
            else:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'login.html', { 'invalid':'invalid inputs' })

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

