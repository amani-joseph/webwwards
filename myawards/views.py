from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username} \n welcome to instagram')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "myawards/auth/register.html", {'form': form})


@login_required
def profile(request):
    context = {
        'posts': Project.objects.filter(user=request.user).all()
    }
    return render(request, 'myawards/auth/profile.html',context )

@login_required
def editProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'myawards/auth/edit_profile.html', context)

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
   
   