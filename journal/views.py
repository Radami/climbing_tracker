from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import SessionSerializer, ClimbSerializer, GradeSerializer
from .models import Session

@api_view(['GET', 'POST'])
def session_list(request, format=None):
    """
    API endpoint that allows sessions to be viewed or edited.
    """
    if request.method == 'GET':
        queryset = Session.objects.all().order_by('-date')
        serializer_class = SessionSerializer(queryset, many=True)
        return Response(serializer_class.data)

    elif request.method == 'POST':
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def session_details(request, pk, format=None):
    try:
        session = Session.objects.get(pk=pk)
    except Session.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SessionSerializer(session)
        return Response(serializer.data)

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