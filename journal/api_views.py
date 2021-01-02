from django.contrib.auth.models import User

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SessionSerializer, UserSerializer, ClimbSerializer
from .models import Session, Climb

# API views
class SessionList(APIView):
    """
    List all climbing sessions or create a new one
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get(self, request, format=None):
        """
        GET method for Sessions
        """
        sessions = Session.objects.all().order_by('-date')
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        POST method for Sessions
        """
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SessionDetails(APIView):
    """
    Retrieve, update or delete a session
    """
    def get_object(self, primary_key):
        """
        Retrieve the object with the specified pk
        """
        try:
            return Session.objects.get(pk=primary_key)
        except Session.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        GET method for Sessions Details
        """
        session = self.get_object(pk)
        serializer = SessionSerializer(session)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        PUT method for Sessions
        """
        session = self.get_object(pk)
        serializer = SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            session.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        DELETE method for Sessions
        """
        session = self.get_object(pk)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClimbList(generics.ListAPIView):
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @api_view(['GET', 'POST'])
# def session_list(request, format=None):
#     """
#     API endpoint that allows sessions to be viewed or edited.
#     """
#     if request.method == 'GET':
#         queryset = Session.objects.all().order_by('-date')
#         serializer_class = SessionSerializer(queryset, many=True)
#         return Response(serializer_class.data)

#     elif request.method == 'POST':
#         serializer = SessionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def session_details(request, pk, format=None):
#     try:
#         session = Session.objects.get(pk=pk)
#     except Session.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = SessionSerializer(session)
#         return Response(serializer.data)




