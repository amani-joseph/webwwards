from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from .models import Project
projects = [{
     'title': '',
     'url': '',
     'description': '',
     'technologies': '',
     'snapshot': '',
     'developer': '',
}]

# Create your views here.
def index(request):
     context = {
        'projects': Project.objects.all(),
    }
     # return HttpResponse('<h1>INDEX ROUTE WORKS</h1>')
     return render(request, 'myawards/home.html', context)