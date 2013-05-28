from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nightjar.views.home', name='home'),
    # url(r'^nightjar/', include('nightjar.foo.urls')),

    url(r'^', include('stories.urls')),
    url(r'^story/(?P<story>\w+)', include('stories.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': '/home/dave/code/nightjar/media/'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
