from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse

from .models import Session, Climb

# Django views
class SessionsIndexView(generic.ListView):
    template_name = 'journal/index.html'
    context_object_name = 'latest_sessions'

    def get_queryset(self):
        """Return the last five climbing sessions"""
        return Session.objects.order_by('-date')[:5]


class SessionsDetailView(generic.DetailView):
    model = Session
    template_name = 'journal/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(SessionsDetailView, self).get_context_data(**kwargs)
        # Add climbs related to this session
        session = Session.objects.get(id=self.kwargs['pk'])
        context['climbs'] = session.climbs.all()
        return context


def rate(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    rating = request.POST['rating']
    session.rating = rating
    session.save()

    return HttpResponseRedirect(reverse('journal:detail', args=(session.id,)))

def add_session(request):
    session = Session()

    center = request.POST['center']
    rating = request.POST['rating']
    date = request.POST['date']

    session.center = center
    session.rating = rating
    session.date = date
    session.owner_id = request.user.id

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
