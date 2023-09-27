from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})