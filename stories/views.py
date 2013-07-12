from django.db.models import Q
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404, redirect

from stories.models import Story
from stories.models import GalleryImage
from blog.models import Post

import random

def get_button_width(buttons,add):
    button_width = 100
    if len(buttons)>0: button_width=100/(len(buttons)+add)
    return button_width-2

def get_size(str,size):
    if len(str)>10:
        if (size>150): size=150
    if len(str)>15:
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

def get_breadcrumbs(s):
    done = False
    crumbs = []
    max_levels = 5
    parent_id = s.parent_id_name
    while not done and max_levels>0:
        try:
            current = Story.objects.get(id_name=parent_id)
            crumbs.append(current)
            max_levels=max_levels+1
            parent_id = current.parent_id_name
#            if parent_id == "main": done = True
        except Story.DoesNotExist:
            done = True
    crumbs.reverse()
    return crumbs

def index(request):
    s = get_object_or_404(Story, id_name='main')
    template = loader.get_template('stories/index.html')
    buttons = Story.objects.filter(parent_id_name='main')
    posts = Post.objects.all().order_by('-date')[:5]
    gallery = GalleryImage.objects.filter(story__id_name='main')

    crumbs = [s]
    calc_button_colours(crumbs)
    calc_button_colours(buttons)
    calc_button_colours(posts)

    context = Context({
        'story': s,
        'buttons': buttons,
        'crumbs': crumbs,
        'button_width': get_button_width(crumbs,0),
        'nav_button_width': get_button_width(buttons,0),
        'button_text_size': calc_button_text_size("","",buttons),
        'gallery': gallery,
        'posts': posts,
        'leaf' : False
    })
    return HttpResponse(template.render(context))

def story(request, story):
    s = get_object_or_404(Story, id_name=story)
    template = loader.get_template('stories/story.html')
    buttons = Story.objects.filter(parent_id_name=story)
    gallery = GalleryImage.objects.filter(story__id_name=story)

    # if no buttons, display buttons on the same level
    if len(buttons)==0:
        buttons = Story.objects.filter(Q(parent_id_name=s.parent_id_name))

    try:
        parent = Story.objects.get(id_name=s.parent_id_name)
    except Story.DoesNotExist:
        # no parents, must be index
        return redirect("/");

    crumbs = get_breadcrumbs(s)
    calc_button_colours(crumbs)
    calc_button_colours(buttons)

    context = Context({
        'story': s,
        'buttons': buttons,
        'crumbs': crumbs,
        'button_width': get_button_width(crumbs,0),
        'nav_button_width': get_button_width(buttons,0),
        'button_text_size': calc_button_text_size(s.title,parent.title,buttons),
        'gallery': gallery,
        'parent': parent,
        'parent_button': random_button(),
        'back_button': random_button()
    })
    return HttpResponse(template.render(context))
