from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    ProjectCreateView,
    ProjectDetailView
)


urlpatterns = [
    path('', views.index, name='index'),
    path('project/new/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='post-detail'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.editProfile, name='edit_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='myawards/auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myawards/home.html'), name='logout'),
]