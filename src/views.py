from django.http import JsonResponse
from django.shortcuts import render
from .models import Message, Project, ProjectImage


def homepage(request):
    return render(request, 'src/index.html')


def contact(request):
    if request.method == 'POST' and request.POST.get('messageTec'):
        sender = request.POST['sender']
        email = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['body']
        msg = Message.objects.create(
            sender=sender, email=email, subject=subject, body=body)
        if msg:
            return JsonResponse({'created': 'Message send successfully! Tec will get back to you ASAP'})
        return JsonResponse({'error': 'not valid'})
    return JsonResponse({'error': 'Post Method Only'})


def projects(request):
    projects = []
    for prj in Project.objects.all():
        projects.append(ProjectImage.objects.filter(
            project_instance__id=prj.id))
    return render(request, 'src/projects.html', {'projects': projects})


def about(request):
    return render(request, 'src/about.html')
