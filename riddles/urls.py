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

    # riddles API
    #riddle/get_riddles_list?categories__name=ca3    włączone filtrowanie na pola
    url(r'api/get_riddles_list', views.RiddleListAPIView.as_view(), name='get_riddles_list_API'),

    url(r'api/get_riddle/(?P<pk>[0-9]+)', views.RiddleDetailAPIView.as_view(), name='get_riddle_API'),
    url(r'api/get_questions/(?P<riddle_pk>[0-9]+)',views.QuestionsListAPIView.as_view(), name='get_questions_list_API'),

    url(r'api/rate_riddle/(?P<pk>[0-9]+)/(?P<new_rate>[0-9]+)', views.RateRiddleAPI.as_view(), name='rate_riddle_API'),
    #api/get_near_riddles/?lat=32.0000&lon=11.000&my_range=10
    url(r'^api/get_near_riddles/$', views.NearRiddleListAPIView.as_view(), name='get_near_list'),

    # Riddles Normal Views
    url(r'^get_riddles_list$', views.riddle_list),
    url(r'^$', views.riddle_list),
    #api/get_near_riddles?lat=32.0000&lon=11.000&my_range=10
    url(r'^get_near_riddles$', views.near_riddle_list),
    url(r'^get_riddle/(?P<pk>[0-9]+)/', views.detail_riddle_view, name='get_riddle'),

    url(r'^questions_view/(?P<pk>[0-9]+)/', views.questions_view),

    # url(r'get_riddles_list', views.RiddleListView.as_view(), name='get_riddles_list'),

]
