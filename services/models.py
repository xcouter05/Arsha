from django.db import models

class Options(models.Model):
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title
    
class Services(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=120)
    image = models.ImageField(upload_to="service",default="default.jpg")
    desc = models.TextField()
    options = models.ManyToManyField(Options)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Features(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=120)
    image = models.ImageField(upload_to="service",default="default.jpg")
    options = models.ManyToManyField(Options)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title 
