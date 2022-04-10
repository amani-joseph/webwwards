from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
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


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'myawards/project_form.html'
    fields = ['title', 'url', 'technologies','snapshot', 'description' ]
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(ProjectCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('index')