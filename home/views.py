from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import projects


# Create your views here.
def index(request):
    project = projects.objects.all()
    return render(request, 'index.html', {'project': project})


def contact(request):
    return render(request, 'contact.html')


def price(request):
    return render(request, 'price.html')


def services(request):
    return render(request, 'services.html')


def about(request):
    return render(request, 'about.html')


def addproject(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        info = request.POST['info']
        completed = request.POST['completed']
        if completed == 1:
            completed = True
        else:
            completed = False
        status = request.POST['status']
        project_instance = projects(title=title, image=image, info=info, completed=completed, status=status)
        project_instance.save()
        return redirect('/')
    return render(request, 'addproject.html')

