# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from rest_framework import generics, filters, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404,get_list_or_404
import django_filters

from .forms import *
from .models import *
from . import serializers


class RiddleFilter(filters.FilterSet,):
    categories = django_filters.CharFilter(name="categories__name")
    min_rate = django_filters.NumberFilter(name="rate", lookup_expr='gte')
    max_rate = django_filters.NumberFilter(name="rate", lookup_expr='lte')

    class Meta:
        model = Riddle
        fields = ['name','description','long','lat','times_resolved','categories','min_rate','max_rate']

#API VIEWS
class RiddleListAPIView(generics.ListAPIView):
    """Returns list of riddles with specific filters"""

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter )
    filter_class = RiddleFilter
    ordering_fields = ('rate', 'times_resolved')
    ordering = ('-times_resolved', )
    search_fields = ('name', 'description')

    serializer_class = serializers.RiddleSerializer

    def get_queryset(self):
        return Riddle.objects.all()




class NearRiddleListAPIView(RiddleListAPIView):
    """return list of riddles in range of given locations"""
    def get_queryset(self):
        request=self.request
        lat, lon, my_range = request.GET.get("lat"), request.GET.get("lon"), request.GET.get("my_range")
        if lat and lon and my_range:
            in_range_list = [t.id for t in Riddle.objects.all()
                             if t.distance((lat, lon), my_range)]
            return Riddle.objects.filter(id__in=in_range_list)
        else:
            return Riddle.objects.all()



class RiddleDetailAPIView(generics.RetrieveAPIView):
    """Returns chosen by id riddle"""

    serializer_class = serializers.RiddleSerializer

    def get_queryset(self):
        return Riddle.objects.all()


class QuestionsListAPIView(generics.ListAPIView):
    """returns all question with answers for specific riddle"""
    serializer_class = serializers.QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter( riddle = self.kwargs['riddle_pk'] )


class RateRiddleAPI(views.APIView):
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

#Normal Views

def riddle_list(request):

    f = RiddleFilter(request.GET, queryset=Riddle.objects.all())
    return render(request, 'riddles/riddle_list.html', {'riddle_list': f})

def near_riddle_list(request):
    f = Riddle.objects.all()
    lat, lon, my_range = request.GET.get("lat"), request.GET.get("lon"), request.GET.get("my_range")
    if lat and lon and my_range:
        in_range_list = [t.id for t in Riddle.objects.all()
                         if t.distance((lat, lon), my_range)]
        f.filter(id__in=in_range_list)

    f = RiddleFilter(request.GET, queryset=f)

    return render(request, 'riddles/riddle_list.html', {'riddle_list': f})

def detail_riddle_view(request, pk):

    riddle = get_object_or_404(
        Riddle,
        id=pk
    )

    photos = Images.objects.filter(riddle=pk)

    return render(request, 'riddles/riddle_detail.html', {'riddle': riddle,'images':photos,})

def start_riddle_view(request, pk):

    riddle = get_object_or_404(
        Riddle,
        id=pk
    )
    return render(request, 'riddles/riddle_map.html', {'riddle': riddle,})

def questions_view(request, pk):
    questions = get_list_or_404(
        Question,
        riddle=pk
    )
    initial_data = []
    for question in questions:
        initial_data.append({
            "question_id": question.id,
            "question_content": question.question
        })
    if request.method == 'POST':
        formset = QuestionsFormSet(request.POST,)
        if request.user.is_authenticated():
            for form in formset:
                if (request.POST.get(form.prefix + '-question_id')):
                    form.fields['answer'].widget.attrs['readonly'] = True

                    question_id = int(request.POST.get(form.prefix + '-question_id'))
                    answer = request.POST.get(form.prefix + '-answer')
                    question_obj = get_object_or_404(Question, id=question_id)
                    if not question_obj or not question_obj.check_answer(answer):
                        form.errors['answer'] = 'Niepoprawna odpowiedz'

                    else:
                        form.errors['answer'] = '+ 100pkt'
        return render(request, 'riddles/questions.html', {'questions': '', "forms": formset})

    if request.method == 'GET':
        formset = QuestionsFormSet(initial=initial_data)
        return render(request, 'riddles/questions.html', {'questions': questions,"forms":formset})
