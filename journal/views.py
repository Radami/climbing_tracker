from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Session

# Create your views here.
def index(request):
    latest_sessions = Session.objects.order_by('date')[:5]
    context = { 'latest_sessions': latest_sessions }
    return render(request, 'journal/index.html', context)

def detail(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    return render(request, 'journal/detail.html', { 'session': session})

def rate(request, session_id):
    session = get_object_or_404(Session, pk=session_id)

    rating = request.POST['rating']
    session.rating = rating
    session.save()

    return HttpResponseRedirect(reverse('journal:detail', args=(session.id,)))
