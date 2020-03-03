from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(template_name='account/login.html'),
         name='login'),
    path('logout/',
         auth_views.LoginView.as_view(template_name='account/logout.html'),
         name='logout'),
    path('registration/', views.registration, name='registration')
]
