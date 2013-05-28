from django.conf.urls.defaults import patterns, url

from stories import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^story/(?P<story>\w+)', views.story, name='story')
)
