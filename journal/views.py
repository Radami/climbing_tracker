from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse

from rest_framework import viewsets

from .serializers import SessionSerializer, ClimbSerializer, GradeSerializer
from .models import Session

class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sessions to be viewed or edited.
    """
    queryset = Session.objects.all().order_by('-date')
    serializer_class = SessionSerializer

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'journal/index.html'
    context_object_name = 'latest_sessions'

    def get_queryset(self):
        """Return the last five climbing sessions"""
        return Session.objects.order_by('date')[:5]


class DetailView(generic.DetailView):
    model = Session
    template_name = 'journal/detail.html'

def rate(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    rating = request.POST['rating']
    session.rating = rating
    session.save()

    return HttpResponseRedirect(reverse('journal:detail', args=(session.id,)))


# Method based views
# def index(request):
#     latest_sessions = Session.objects.order_by('date')[:5]
#     context = { 'latest_sessions': latest_sessions }
#     return render(request, 'journal/index.html', context)

# def detail(request, session_id):
#     session = get_object_or_404(Session, pk=session_id)
#     return render(request, 'journal/detail.html', { 'session': session})