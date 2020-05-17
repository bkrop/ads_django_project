from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #jeżeli method == POST to form przyjmuje to co jest wpisane
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #tylko w celu wyświetlenia poniżej
            messages.success(request, f'Account created for {username}')
            return redirect('ads-home')
    else:
        form = UserRegisterForm() #jeżeli GET to form jest puste
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    context = {'ads': request.user.ad_set.all()} #request.user = current_user
    return render(request, 'users/profile.html', context)
