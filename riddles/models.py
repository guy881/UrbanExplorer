from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
import math

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name

class Riddle(models.Model):
    name = models.CharField(
        _('name'),
        max_length=50,
    )

    description = models.TextField(
        _('description')
    )

    long = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )
    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )
    times_resolved = models.DecimalField(
        max_digits=9,
        decimal_places=0,
        default=0
    )
    rate = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        default=0
    )

    logo_image = models.ImageField(
        _('logo image'),
        upload_to='pic/logos',
        null=True,
        blank=True
    )
    min_image = models.ImageField(
        _('min image'),
        upload_to='pic/min_logos',
        null=True,
        blank=True
    )

    categories = models.ManyToManyField(Category)


    def __str__(self):
        return self.name

    def rate_riddle(self, rate):
        self.rate = (self.times_resolved * self.rate + int(rate)) / (self.times_resolved + 1)
        self.times_resolved += 1
        self.save()

    def distance(self, destination, my_range):
        lat1, lon1 = float(self.lat), float(self.long)
        lat2, lon2 = destination
        lat2, lon2=float(lat2), float(lon2)
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d < float(my_range)

    # questions z klasy questions
    #     riddle_obj.question_set.all()
    #category z klasy Category


class Question(models.Model):
    riddle = models.ForeignKey(Riddle, db_index=True)

    question = models.CharField(max_length=240, db_index=True)
    answer = models.CharField(max_length=240)

    def __str__(self):
        return self.question

    def check_answer(self, given_ans):
        if given_ans.lower() == self.answer.lower():
            return True
        else:
            return False



class Images(models.Model):
    riddle = models.ForeignKey(Riddle, db_index=True)

    register_image = models.ImageField(
        _('pic/register image'),
        upload_to='register_images',
        null=True,
        blank=True
    )
