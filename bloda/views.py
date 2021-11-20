from django.shortcuts import render
from .forms import Post

# Create your views here.

def PostView(request):
     form = Post
     return render(request, "addpost.html",{'form':form})
