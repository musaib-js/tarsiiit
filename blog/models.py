from django.db import models

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    desc = models.TextField()
    img = models.ImageField(upload_to = 'media')
    slug = models.CharField(max_length = 250, default = "nothing-yet")
    is_featured = models.BooleanField(default=False)


    def __str__(self):
        return self.title + " by " + self.author



    
