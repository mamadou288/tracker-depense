from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'tracker/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'tracker/register.html', {'form': form})

@login_required
def ajouter_depense(request):
    pass
    # View logic

@login_required
def lister_depenses(request):
    # View logic
    pass
