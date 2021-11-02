from django.db import models

# Create your models here.
class Research(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 300)
    desc = models.TextField()
    img = models.ImageField(upload_to = 'media')

    def __str__(self):
        return self.title
        