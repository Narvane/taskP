from django.shortcuts import render
from Tasks.models import *

# Create your views here.
def home(request):
    tasks = Task.objects.order_by('-title')[:5]
    tak = Task.objects.get(pk=1)
    context = {
        'Tasks': tasks,
        'tak': tak
    }
    return render(request, "index.html", context)
