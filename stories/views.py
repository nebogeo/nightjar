from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, redirect

from stories.models import Story
from stories.models import GalleryImage
from blog.models import Post

button_colours = ["#ff7777", "#77ff77", "#7777ff", "#00ffff", "#ff00ff"];

def get_button_width(buttons,add):
    button_width = 100
    if len(buttons)>0: button_width=100/(len(buttons)+add)
    button_width -= 2
    return button_width

def index(request):
    s = get_object_or_404(Story, id_name='main')
    template = loader.get_template('stories/index.html')
    buttons = Story.objects.filter(parent_id_name='main')
    posts = Post.objects.all().order_by('-date')[:5]
    c=0
    for button in buttons:
        button.colour=button_colours[c];
        button.size=100;
        if len(button.title)>11:
            button.size=75;
        c=c+1
    context = Context({
        'story': s,
        'buttons': buttons,
        'button_width': get_button_width(buttons,0),
        'posts': posts
    })
    return HttpResponse(template.render(context))


def story(request, story):
    s = get_object_or_404(Story, id_name=story)
    template = loader.get_template('stories/story.html')
    buttons = Story.objects.filter(parent_id_name=story)
    # if no buttons, display buttons on the same level
    if len(buttons)==0:
        buttons = Story.objects.filter(parent_id_name=s.parent_id_name)

    gallery = GalleryImage.objects.filter(story__id_name=story)
    try:
        parent = Story.objects.get(id_name=s.parent_id_name)
    except Story.DoesNotExist:
        # no parents, must be index
        return redirect("/");
    c=0
    for button in buttons:
        button.colour=button_colours[c];
        button.size=100;
        if len(button.title)>11:
            button.size=75;
        c=c+1
    context = Context({
        'story': s,
        'buttons': buttons,
        'button_width': get_button_width(buttons,1),
        'gallery': gallery,
        'parent': parent
    })
    return HttpResponse(template.render(context))
