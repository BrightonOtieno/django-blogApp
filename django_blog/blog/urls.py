from django.contrib import admin
from django.urls import path
from .views import PostListView, post_detail_view,PostCreateView,PostUpdateView,PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(),name = "blog-home"),
    path('post/new/', PostCreateView.as_view(),name = "create-post"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name = "update-post"),
    path('user/<str:username>/',  UserPostListView.as_view(),name = "user-post"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name = "delete-post"),
    path('post/<int:id>/detail/',post_detail_view,name = "post-detail"),
]
