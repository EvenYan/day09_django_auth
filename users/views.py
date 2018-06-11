from django.shortcuts import render, redirect

# Create your views here.
from users.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'users/register.html', context={'form': form})

def index(request):
    return render(request, 'users/index.html')