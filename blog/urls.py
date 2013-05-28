from django.conf.urls.defaults import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^blog/', views.index, name='blog'),
    url(r'^post/(?P<post_id>\d+)', views.post, name='post')
)
