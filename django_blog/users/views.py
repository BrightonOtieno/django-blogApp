from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account createdfor {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    context ={
        "form":form
    }

    return render(request,"users/user_registration_page.html", context)