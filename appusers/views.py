from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
def mark_as_done(request, pk):
    task = get_object_or_404(AppUser, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def deleteTask(request,pk):

    task = get_object_or_404(AppUser,pk=pk)
    task.delete()
    return redirect('home')

def mark_as_undone(request,pk):

    task = get_object_or_404(AppUser,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request,pk):

    if request.method == 'POST':
        get_task = get_object_or_404(AppUser,pk=pk)
        get_task.task = request.POST.get('task')
        get_task.save()
        return redirect('home')
    else:
        get_task = get_object_or_404(AppUser, pk=pk)
        context = {'get_task': get_task}
        return render(request, 'edit_task.html',context)
    
def resetTasks(request):

    get_tasks = AppUser.objects.all()

    if get_tasks:
        get_tasks.delete()
        return redirect('home')
    else:
        return HttpResponse("No tasks to reset.")