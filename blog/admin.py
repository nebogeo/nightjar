from django.contrib import admin
from blog.models import *

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Category)
admin.site.register(PostCategory)
