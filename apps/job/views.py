from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddJobForm
from .models import Job


@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)


        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('all_jobs')
    else:
        form = AddJobForm()

    return render(request, 'add_job.html', {'form': form})
