from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from .models import Event, Match

# Create your views here.
# def index(request):
#     upcoming_events = Event.objects.order_by('date')[:10]
#     context = {'upcoming_events': upcoming_events}
#     return render(request, 'events/index.html', context)

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'upcoming_events'

    def get_queryset(self):
        """Return the last five published events."""
        return Event.objects.order_by('date')[:7]


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'


def match(request, id):
    #pull fighters from the match and displays a page with the
    match = get_object_or_404(Match, id = id)
    return render(request, 'events/match.html', {'match': match,
                                                'wrestlers': wrestlers})
