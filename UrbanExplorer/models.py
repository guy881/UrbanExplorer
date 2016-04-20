from __future__ import unicode_literals

from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Riddle(models.Model):
    name = models.CharField(max_length=100)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)  # every riddle is assigned to particular venue
    category = models.CharField(max_length=40)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    # After changing model run: python manage.py makemigrations UrbanExplorer
