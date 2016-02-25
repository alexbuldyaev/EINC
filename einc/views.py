from django.shortcuts import render

def post_list(request):
    return render(request, 'einc/post_list.html', {})
