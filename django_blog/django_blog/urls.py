
from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('profile/',user_views.user_profile_view ,name="user-profile"),
    path('registration/',user_views.user_registration_view , name="registration-page"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html') , name="login-page"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout-page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
