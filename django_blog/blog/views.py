from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.
"""
def home_page_view(request):

    obj = Post.objects.all()
    context = {
        "posts":obj,
        "title":'Blog-Home-Page'
    }


    return render(request,"blog/index.html",context)
"""
class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering =['-date_posted']
    paginate_by = 3

# Custom User List of Posts 
class UserPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    #ordering =['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User,username=username)
        return Post.objects.filter(author=user).order_by('-date_posted')


# post detail view 
def post_detail_view(request, id):
    obj = get_object_or_404(Post, id= id)

    context ={
        "post":obj
    }

    return render(request,"blog/post_detail_page.html", context)

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ['title','content']


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ['title','content']


    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(DeleteView):
    model = Post
    #template_name = ".html"
    success_url ='/'
    def test_func(self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
