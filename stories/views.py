from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from stories.models import Story
from stories.models import GalleryImage
from blog.models import Post

def get_button_width(buttons):
    button_width = 100
    if len(buttons)>0: button_width=100/(len(buttons)+1)
    button_width -= 2
    return button_width

def index(request):
    s = get_object_or_404(Story, id_name='main')
    template = loader.get_template('stories/index.html')
    buttons = Story.objects.filter(parent_id_name='main')
    posts = Post.objects.all().order_by('-date')[:5]

    context = Context({
        'story': s,
        'buttons': buttons,
        'button_width': get_button_width(buttons),
        'posts': posts
    })
    return HttpResponse(template.render(context))


def story(request, story):
    s = get_object_or_404(Story, id_name=story)
    template = loader.get_template('stories/story.html')
    buttons = Story.objects.filter(parent_id_name=story)
    gallery = GalleryImage.objects.filter(story__id_name=story)
    parent = get_object_or_404(Story, id_name=s.parent_id_name)

    context = Context({
        'story': s,
        'buttons': buttons,
        'button_width': get_button_width(buttons),
        'gallery': gallery,
        'parent': parent
    })
    return HttpResponse(template.render(context))
