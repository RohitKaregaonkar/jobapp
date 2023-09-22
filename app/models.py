from django.db import models
from django.utils.text import slugify

# Create your models here.
class Location(models.Model):
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    zip = models.CharField(max_length=120)

class Authors(models.Model):
    name = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    designation = models.CharField(max_length=120)


class JobPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    creation_date = models.DateTimeField(auto_now_add=True)
    expiry_date =  models.DateTimeField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)
