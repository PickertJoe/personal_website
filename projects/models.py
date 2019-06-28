from django.db import models

# Create your models here.


class Project(models.Model):
    """Used for displaying projects of interest on personal website"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    link = models.URLField(default='')

    def __str__(self):
        return self.title
