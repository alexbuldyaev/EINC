from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    return render(request, 'einc/results.html', {})

def post_count(request):
    return render(request, 'einc/count.html', {})
def post_countksk(request):
    return render(request, 'einc/countksk.html', {})
def post_counthom(request):
    return render(request, 'einc/counthome.html', {})
def post_signin(request):
    return render(request, 'einc/signin.html', {})
def post_bepay(request):
    return render(request, 'einc/bepay.html', {})


