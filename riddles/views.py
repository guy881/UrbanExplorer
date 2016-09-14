from django.shortcuts import render

# Create your views here.

from rest_framework import generics, filters, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import django_filters


from .models import *
from . import serializers


class RiddleFilter(filters.FilterSet,):
    categories = django_filters.CharFilter(name="categories__name")
    min_rate = django_filters.NumberFilter(name="rate", lookup_expr='gte')
    max_rate = django_filters.NumberFilter(name="rate", lookup_expr='lte')

    class Meta:
        model = Riddle
        fields = ['name','description','long','lat','times_resolved','categories','min_rate','max_rate']


class RiddleListView(generics.ListAPIView):
    """Returns list of riddles with specific filters"""

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter )
    filter_class = RiddleFilter
    ordering_fields = ('rate', 'times_resolved')
    ordering = ('-times_resolved', )
    search_fields = ('name', 'description')

    serializer_class = serializers.RiddleSerializer

    def get_queryset(self):
        return Riddle.objects.all()




class NearRiddleListView(RiddleListView):
    """return list of riddles in range of given locations"""
    def get_queryset(self):
        in_range_list = [t.id for t in Riddle.objects.all()
                            if t.distance(
                                (float(self.kwargs['lat']), float(self.kwargs['lon'])),
                                float(self.kwargs['my_range'])
                            )
                ]

        return Riddle.objects.filter(id__in = in_range_list)


class RiddleDetailView(generics.RetrieveAPIView):
    """Returns chosen by id riddle"""

    serializer_class = serializers.RiddleSerializer

    def get_queryset(self):
        return Riddle.objects.all()


class QuestionsListView(generics.ListAPIView):
    """returns all question with answers for specific riddle"""
    serializer_class = serializers.QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter( riddle = self.kwargs['riddle_pk'] )


class RateRiddle(views.APIView):
    """Rate riddle and calculate values"""

    def put(self, request, pk , new_rate):

        riddle = get_object_or_404(
            Riddle,
            id = pk
        )

        riddle.rate_riddle(int(new_rate))

        return Response({
            'status': 0,
        })
