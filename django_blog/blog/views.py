from django.shortcuts import render,get_object_or_404
from .models import Post

# Create your views here.

def home_page_view(request):

    obj = Post.objects.all()
    context = {
        "posts":obj,
        "title":'Blog-Home-Page'
    }

    return render(request,"blog/index.html",context)

# post detail view 
def post_detail_view(request, id):
    obj = get_object_or_404(Post, id= id)

    context ={
        "post":obj
    }

    return render(request,"blog/post_detail_page.html", context)
