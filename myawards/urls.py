from django.urls import path, include
from . import views
from .views import (
    ProjectCreateView,
)


urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', ProjectCreateView.as_view(), name='project_create'),
]