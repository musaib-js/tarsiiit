from django.db import models

# Create your models here.
class Event(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 250)
    date = models.DateTimeField()
    desc = models.TextField()
    img = models.ImageField(upload_to = 'media')
    video = models.FileField(upload_to = 'media')

    def __str__(self):
        return self.title
