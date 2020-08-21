from django.shortcuts import render
from .models import Post

# Create your views here.

def home_page_view(request):

    obj = Post.objects.all()
    context = {
        "posts":obj,
        "title":'Blog-Home-Page'
    }

    return render(request,"blog/index.html",context)
