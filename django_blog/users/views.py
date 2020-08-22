from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account createdfor {username}!')
            return redirect('login-page')
    else:
        form = UserRegisterForm()

    context ={
        "form":form
    }

    return render(request,"users/user_registration_page.html", context)

@login_required
def user_profile_view(request):

    return render(request,'users/user_profile.html')
