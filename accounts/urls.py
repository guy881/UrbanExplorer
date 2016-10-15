# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^api/login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^api/register/$', UserCreateAPIView.as_view(), name='register'),

    url(r'^accounts/profile/$', profile_view, name='profile'),
]
