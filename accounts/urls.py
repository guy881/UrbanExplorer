# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^api/login/$', UserLoginAPIView.as_view(), name='api_login'),
    url(r'^api/register/$', UserCreateAPIView.as_view(), name='api_register'),

    url(r'^accounts/profile/$', profile_view, name='profile'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
]
