from django.shortcuts import render

def post_list(request):
    return render(request, 'einc/results.html', {})

def post_count(request):
    return render(request, 'einc/count.html', {})
