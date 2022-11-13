from django.db import models

# Create your models here.
class Research(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 300)
    slug = models.CharField(max_length=350, default="nothing-yet")
    is_featured = models.BooleanField(default=False)
    desc = models.TextField()
    img = models.ImageField(upload_to = 'media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Research"
        