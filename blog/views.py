from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.filter(author = 1)
    return render(request, "blog/index.html", {"posts": posts})