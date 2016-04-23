from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Riddle, Venue
from django.template import loader
# Create your views here.

def index(request):
    riddles = Riddle.objects.order_by("-name")
    context = {
        'riddles_list': riddles,    # name used in index.html template
    }
    return render(request, 'UrbanExplorer/index.html', context)

def venue(request, venue_id):
    try:
        venue = Venue.objects.get(pk=venue_id)
    except Venue.DoesNotExist:
        raise Http404('No venue with such id!')

    #shorter way:
    venue = get_object_or_404(Venue, pk=venue_id)
    return HttpResponse("Details about venue: " + str(venue))

def riddle(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk=riddle_id)
    return HttpResponse("Details about riddle: " + str(riddle))