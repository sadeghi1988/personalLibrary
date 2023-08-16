from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='login'),
    path('create/', views.create_account, name='create'),
    path('home/', views.home, name='home'),
]