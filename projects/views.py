from django.shortcuts import render
from projects.models import Project


# Create your views here.

def project_index(request):
    """Provides a snippet of information for each project"""
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    """Provides more specific information for an individual project"""
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'project_detail.html', context)
