from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    message = 'Hello User, you are on the projects page'
    return render(request, 'projects.html', {'message': message})

def project(request, primary_key):
    page_message = f'You are on the page {primary_key} of projects'
    welcome_message = 'Thank you for visiting this page'
    return render(request, 'single-project.html', {
        'page': page_message,
        'welcome': welcome_message
    })