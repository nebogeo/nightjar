from django.db import models
from django.contrib.auth.models import User

# the main story model
class Story(models.Model):
    title = models.CharField(max_length=200)
    id_name = models.CharField(max_length=200)
    parent_id_name = models.CharField(max_length=200)
    desc = models.TextField()

    def __unicode__(self):
        return self.id_name;

    class Meta:
        verbose_name_plural = "Stories"

# multiple images per story
class GalleryImage(models.Model):
    story = models.ForeignKey(Story)
    image = models.ImageField(blank=True, null=True, upload_to="gallery_images")
    desc = models.TextField(blank=True)
    embed = models.TextField(blank=True)

    def __unicode__(self):
        if (self.image): return self.story.id_name+" "+self.image.url;
        else: return self.story.id_name+" video";
