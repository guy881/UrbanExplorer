# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth import get_user_model

import json
import requests
from django.template import  RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logut


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
#
# from posts.api.permissions import IsOwnerOrReadOnly
# from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination
#
#



User = get_user_model()


from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]




class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
#Views
from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import *

def profile_view(request):
    if request.user.id:
        acc = get_object_or_404(
            Account,
            id=request.user.pk
        )
        form = ProfileForm()

        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES, instance=acc)
            if request.user.is_authenticated():
                if form.is_valid():
                    # acc.profile_picture.delete()
                    #TODO:trzeba by ogarnać jak kasować zdjęcia z bazy
                    form.save()


        return render(request, 'profile.html', {'user': acc,'form':form})
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


def login(request):
    error = ''

    if request.method == "POST":
        #TODO zmienić na dynamiczny link
        login = requests.post('http://127.0.0.1:8000' + reverse('accounts:api_login'),
                              data={'username': request.POST['username'], 'password': request.POST['password']})
        response = json.loads(login.text)

        if response.get('non_field_errors', False):
            error = response['non_field_errors']
        elif response.get('token', False) and response.get('username', False):
            username = response.get('username')
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect("/accounts/profile")
    return render_to_response("login.html", {"error": error}, RequestContext(request))


def logout(request):
    auth_logut(request)
    return HttpResponseRedirect('/')