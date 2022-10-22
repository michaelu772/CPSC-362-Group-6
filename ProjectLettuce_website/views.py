from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from apps.job.models import Job




def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def login(request):
    return render(request, "accounts/login.html")

def all_jobs(request):
    jobs = Job.objects.all()[0:3]
    return render(request, 'all_jobs.html', {'jobs': jobs})

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)

            return redirect('profile')


    context = {'form' :form}
    return render(request, "accounts/register.html", context)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"




