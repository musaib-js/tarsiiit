from django.db import models

# Create your models here.
class Team(models.Model):
    sno= models.AutoField(primary_key = True)
    name =  models.CharField(max_length = 200)
    designation = models.CharField(max_length = 200, default = "")
    img = models.ImageField(upload_to = 'media')
    desc = models.TextField()
    fb_link = models.URLField()
    twitter_link = models.URLField()
    linkedin_link = models.URLField()
    googleplus_link = models.URLField()

    def __str__(self):
        return self.name
    