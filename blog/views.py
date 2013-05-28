# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from blog.models import Post

def index(request):
    template = loader.get_template('blog/index.html')
    posts = Post.objects.all().order_by('-date')[:5]
    context = Context({
        'posts': posts
    })
    return HttpResponse(template.render(context))


def post(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    template = loader.get_template('blog/post.html')
    context = Context({
        'post': p
    })
    return HttpResponse(template.render(context))
