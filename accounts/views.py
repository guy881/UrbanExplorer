from django.db.models import Q
from django.contrib.auth import get_user_model


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
                #trzeba by ogarnać jak kasować zdjęcia z bazy
                form.save()


    return render(request, 'profile.html', {'user': acc,'form':form})
