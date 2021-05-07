'''
Views for climbing journal app
'''
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Session, Climb, Grade

# Django views
class SessionsIndexView(generic.ListView):
    '''
        Class based Index View for Sessions
    '''
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

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'journal/index.html')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)

def add_climb(request):
    #TODO: validation on user and session
   
    climb = Climb()

    grade_label = request.POST['grade']
    climb.grade =  Grade.objects.get(label=grade_label)
    climb.comments = request.POST['comments']
    climb.rating = request.POST['rating']
    session_id = request.POST['session']
    climb.session = Session.objects.get(id=session_id)
    climb.owner_id = request.user.id

    climb.save()

    return HttpResponseRedirect(reverse('journal:detail', args=(climb.session_id,)))

def delete_climb(request):
    #TODO: validate permissions
    climb = Climb.objects.get(id=request.POST['climb_id'])
    climb.delete()

    return HttpResponseRedirect(reverse('journal:detail', args=(climb.session_id,)))

# Method based views
# def index(request):
#     latest_sessions = Session.objects.order_by('date')[:5]
#     context = { 'latest_sessions': latest_sessions }
#     return render(request, 'journal/index.html', context)

# def detail(request, session_id):
#     session = get_object_or_404(Session, pk=session_id)
#     return render(request, 'journal/detail.html', { 'session': session})
