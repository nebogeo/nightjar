from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from stories.models import Story
from stories.models import StoryImage
from blog.models import Post

def index(request):
    s = get_object_or_404(Story, id_name='main')
    template = loader.get_template('stories/index.html')
    buttons = Story.objects.filter(parent_id_name='main')
    posts = Post.objects.all().order_by('-date')[:5]

    context = Context({
        'story': s,
        'buttons': buttons,
        'posts': posts
    })
    return HttpResponse(template.render(context))


def story(request, story):
    s = get_object_or_404(Story, id_name=story)
    template = loader.get_template('stories/story.html')
    buttons = Story.objects.filter(parent_id_name=story)
    gallery = StoryImage.objects.filter(story__id_name=story)

    button_width = 10
    if len(buttons)>0: button_width=100/len(buttons)
    button_width -= 2

    context = Context({
        'story': s,
        'buttons': buttons,
        'button_width': button_width,
        'gallery': gallery
    })
    return HttpResponse(template.render(context))
