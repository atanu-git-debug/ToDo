from django.http import HttpResponse
from django.shortcuts import redirect, render

from appusers.models import AppUser

# Create your views here.
def addTask(request):
    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            AppUser.objects.create(task=task)
        # Here you would typically save the task to the database
        
        return redirect('home')  # Redirect to home or another page after adding the task
    return HttpResponse("Invalid request method.")