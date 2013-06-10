from django.db import models

# the main story model
class Story(models.Model):
    title = models.CharField(max_length=200)
    id_name = models.CharField(max_length=200)
    parent_id_name = models.CharField(max_length=200)
    desc = models.TextField()
    desc_image = models.ImageField(upload_to="story_images")
    button_image = models.ImageField(upload_to="story_images")

    def __unicode__(self):
        return self.id_name;

    class Meta:
        verbose_name_plural = "Stories"

# multiple images per story
class StoryImage(models.Model):
    story = models.ForeignKey(Story)
    image = models.ImageField(upload_to="story_images")
    desc = models.TextField(blank=True)

    def __unicode__(self):
        return self.story.__unicode__();
