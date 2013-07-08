from django.db.models import Q
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, redirect

from stories.models import Story
from stories.models import GalleryImage
from blog.models import Post

import random

def get_button_width(buttons,add):
    button_width = 90
    if len(buttons)>0: button_width=90/(len(buttons)+add)
    return button_width

def get_size(str,size):
    if len(str)>9:
        if (size>150): size=150
    if len(str)>13:
        size=130
    return size

def calc_button_text_size(title, parent_title, buttons):
    size=150
#    for button in buttons:
#        size=get_size(button.title,size)

#    size=get_size(title,size)
#    size=get_size(parent_title,size)
    return size

def random_button():
    return "button-"+"%02d"%random.randrange(1,10)+".png";

def calc_button_colours(buttons):
    for button in buttons:
        button.image=random_button()

def index(request):
    s = get_object_or_404(Story, id_name='main')
    template = loader.get_template('stories/index.html')
    buttons = Story.objects.filter(parent_id_name='main')
    posts = Post.objects.all().order_by('-date')[:5]
    calc_button_colours(buttons)
    context = Context({
        'story': s,
        'buttons': buttons,
        'button_width': get_button_width(buttons,0),
        'button_text_size': calc_button_text_size("","",buttons),
        'posts': posts,
        'leaf' : False
    })
    return HttpResponse(template.render(context))


def story(request, story):
    s = get_object_or_404(Story, id_name=story)
    template = loader.get_template('stories/story.html')

    buttons = Story.objects.filter(parent_id_name=story)

    # if no buttons, display buttons on the same level
    leaf=False
    if len(buttons)==0:
        leaf=True
        buttons = Story.objects.filter(Q(parent_id_name=s.parent_id_name))

    gallery = GalleryImage.objects.filter(story__id_name=story)

    try:
        parent = Story.objects.get(id_name=s.parent_id_name)
    except Story.DoesNotExist:
        # no parents, must be index
        return redirect("/");

    button_width = get_button_width(buttons,1);
    if leaf: button_width=get_button_width(buttons,1);

    calc_button_colours(buttons)
    context = Context({
        'story': s,
        'buttons': buttons,
        'button_width': button_width,
        'button_text_size': calc_button_text_size(s.title,parent.title,buttons),
        'gallery': gallery,
        'parent': parent,
        'parent_button': random_button(),
        'back_button': random_button(),
        'leaf': leaf
    })
    return HttpResponse(template.render(context))
