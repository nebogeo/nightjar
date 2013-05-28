from django.db import models
from django.contrib.auth.models import User

# a simple blog post
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField('date published')
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.title;

# multiple images per blog post
class PostImage(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to="blog_images")
    def __unicode__(self):
        return self.image;

# categories
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name;
    class Meta:
        verbose_name_plural = "Categories"

# categories assigned to posts (multiple per post)
class PostCategory(models.Model):
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)
    class Meta:
        verbose_name_plural = "Post Categories"
