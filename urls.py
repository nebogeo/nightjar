from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('stories.urls')),
    url(r'^story/(?P<story>\w+)', include('stories.urls')),
    url(r'^', include('blog.urls')),
    url(r'^post/(?P<post_id>\d+)', include('blog.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': '/home/dave/code/nightjar/media/'}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': '/home/dave/code/nightjar/static/'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
