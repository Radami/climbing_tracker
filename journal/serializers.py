from .models import Session, Climb, Grade
from rest_framework import serializers

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = [ 'center', 'date', 'rating' ] 

class ClimbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Climb
        fields = [ 'grade', 'comments', 'rating', 'session' ]

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = [ 'label', 'weight' ]