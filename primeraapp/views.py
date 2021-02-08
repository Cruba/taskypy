from django.shortcuts import render
from primeraapp.models import Post

# Create your views here.

def home(request):
    return render(request, 'post/index.html', 
    {'posts':Post.objects.count()} )

def post_list (request):
   # posts= Post.objects.all()
    posts= Post.objects.filter(
        status='Published',
    )

    return render(request, 'post/index.html', {'posts':posts})