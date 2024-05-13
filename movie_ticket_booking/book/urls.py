from django.urls import path
from . import views
from . views import home

urlpatterns = [
    path('', home, name='home'),
    path('api/movies/', views.api_movies, name='api_movies'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.custom_logout, name='logout'),
]
