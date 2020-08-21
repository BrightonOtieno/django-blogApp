from django.urls import path
from .views import user_registration_view


urlpatterns = [
    path('registration/',user_registration_view, name='user-registration-page'),
]

