from __future__ import unicode_literals
from django.db.models.signals import *

from django.db import models
from riddles.models import *
# Create your models here.
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    solved_riddles = models.ManyToManyField(Riddle)

    lvl = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        default=1
    )
    expirience = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        default=0
    )

    def add_experience(self, added):
        level_tab=[1000,2500,5000,10000,17500,27500]
        self.expirience += added
        for idx,item in enumerate(level_tab[:-1]):
            if self.expirience>item:
                if self.lvl < idx+1:
                    self.lvl=idx+1
                    return True
        return False

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(userName=instance)

post_save.connect(create_user_profile, sender=User)
