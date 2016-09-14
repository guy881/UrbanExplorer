# -*- coding: utf-8 -*-

"""Urban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # riddles
    #riddle/get_riddles_list?categories__name=ca3    włączone filtrowanie na pola
    url(r'get_riddles_list', views.RiddleListView.as_view(), name='get_riddles_list'),

    url(r'get_riddle/(?P<pk>[0-9]+)', views.RiddleDetailView.as_view(), name='get_riddle'),
    url(r'get_questions/(?P<riddle_pk>[0-9]+)',views.QuestionsListView.as_view(), name='get_questions_list'),

    url(r'api/rate_riddle/(?P<pk>[0-9]+)/(?P<new_rate>[0-9]+)', views.RateRiddle.as_view(), name='rate_riddle'),
    #riddle/get_near_riddles/32.0000/11.000/10/
    url(r'api/get_near_riddles/(?P<lat>[0-9]+\.?[0-9]+)/(?P<lon>[0-9]+\.?[0-9]+)/(?P<my_range>[0-9]+\.?[0-9]+)/', views.NearRiddleListView.as_view(), name='get_near_list'),

    # models

]
