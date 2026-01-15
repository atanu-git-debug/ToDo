from django.shortcuts import render

from appusers.models import AppUser

def home(request):

    tasks = AppUser.objects.filter(is_completed=False).order_by('-updated_at')
    
    
    context={
        'tasks': tasks
    }
    return render(request, 'home.html', context)