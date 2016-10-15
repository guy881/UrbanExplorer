# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models import Prefetch
from django.core.urlresolvers import reverse

from rest_framework import serializers

from . import models
from riddles.models import *

class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)

class QuestionSerializer(serializers.ModelSerializer):
    """questions for specific riddle"""
    class Meta:
        model = Question
        fields = ('question', 'answer','id')

    def __str__(self):
        return self.name

class RiddleSerializer(serializers.ModelSerializer):
    """serialize riddle"""

    # logo_image =serializers.SerializerMethodField()
    min_image =serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Riddle
        fields = ('name','description','long','lat','times_resolved','rate','min_image','categories','id')

    # def get_logo_image(self, instance):
    #     return str(instance.logo_image) or False

    def get_min_image(self, instance):
        return str(instance.min_image) or False

    def get_categories(self, instance):
        serializer = CategoriesSerializer(
            instance.categories,
            many=True,
        )
        return serializer.data

    def __str__(self):
        return self.name



