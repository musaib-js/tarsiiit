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

    class Meta:
        verbose_name_plural = "Team"
    
class Gallery(models.Model):
    sno= models.AutoField(primary_key = True)
    img = models.ImageField(upload_to = "media")

    class Meta:
        verbose_name_plural = "Gallery"

class Contact(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=245)
    subject = models.CharField(max_length=240)
    message = models.TextField()

    def __str__(self):
        return "Query By " + self.name

class Recruitment_Query(models.Model):
    name = models.CharField(max_length=240)
    college_id = models.CharField(max_length =  10)
    branch = models.CharField(max_length = 15)
    whatsapp = models.CharField(max_length = 12)
    proposal = models.TextField()

    def __str__(self):
        return "Proposal By " + self.name + " from " + self.branch

    class Meta:
        verbose_name_plural = "Recruitment Queries"
    
    