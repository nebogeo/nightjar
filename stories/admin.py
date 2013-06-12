from django.contrib import admin
from stories.models import *

admin.site.register(Story)
admin.site.register(GalleryImage)
admin.site.register(GalleryVideo)
