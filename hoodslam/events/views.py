from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    upcoming_events = Events.objects.order_by('date')[:10]
    context = {'upcoming_events':upcoming_events }
    return render(request, 'events/index.html',context)

def match(request, id):
    #pull fighters from the match and displays a page with the
    match = get_object_or_404(Match, id = id)
    return render(request, 'events/match.html', {'match': match,
                                                'wrestlers': wrestlers})


# def index(request):
#     latest_wrestlers_list = Wrestler.objects.order_by('wins')[:10]
#     context = {'latest_wrestlers_list': latest_wrestlers_list}
#     return render(request, 'wrestlers/index.html', context )
