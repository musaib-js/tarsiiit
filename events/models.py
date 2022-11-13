from django.db import models

# Create your models here.
class Event(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 250)
    date = models.DateTimeField()
    desc = models.TextField()
    slug = models.CharField(max_length = 250, default = "nothing-yet")
    registrations_open= models.BooleanField(default=True)
    is_conducted = models.BooleanField(default=False)
    img = models.ImageField(upload_to = 'media')
    video = models.FileField(upload_to = 'media')

    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.CharField(max_length = 250)
    name = models.CharField(max_length = 200)
    id_no = models.CharField(max_length  = 10)
    branch = models.CharField(max_length=20)
    batch = models.CharField(max_length = 20)

    def __str__(self):
        return self.event + " by " + self.name
    
