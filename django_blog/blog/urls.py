from django.contrib import admin
from django.urls import path
from .views import home_page_view, post_detail_view

urlpatterns = [
    path('',home_page_view,name = "blog-home"),
    path('<int:id>/detail/',post_detail_view,name = "post-detail"),
]
