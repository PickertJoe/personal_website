from django.db import models

# Create your models here.


class Project(models.Model):
    """Used for displaying projects of interest on personal website"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='/img')
