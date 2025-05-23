from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.core.paginator import Paginator
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from .models import *

def home(request):
    return render(request, 'registro/index.html')

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context={'form':form}
    return render(request, 'registro/register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                #bot.send_message(chat_id, text='Logueado')
                return redirect('dashboard')
    context = {'form':form}
    return render(request, 'registro/my-login.html', context=context)

@login_required(login_url='my-login')
def dashboard(request):
    periodicos_all = Periodico.objects.all()
    paginator = Paginator(periodicos_all, 20)
    page = request.GET.get('page')
    periodicos = paginator.get_page(page)
    context = {
        'periodicos':periodicos,
    }
    return render(request, 'app/dashboard.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect('my-login')