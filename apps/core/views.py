from django.shortcuts import render

from apps.job.models import Job

def frontpage(request):
    jobs = Job.objects.all()[0:3]
    return render(request, 'ProjectLettuce_website/templates/all_jobs.html', {'jobs': jobs})
