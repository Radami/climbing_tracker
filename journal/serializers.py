from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Session, Climb, Grade


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    climbs = serializers.PrimaryKeyRelatedField(many=True, queryset=Climb.objects.all())
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Session
        fields = [ 'center', 'date', 'rating', 'climbs', 'owner']

class ClimbSerializer(serializers.HyperlinkedModelSerializer):
    session = serializers.PrimaryKeyRelatedField(many=False, queryset=Session.objects.all())
    grade = serializers.PrimaryKeyRelatedField(many=False, queryset=Grade.objects.all())
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Climb
        fields = [ 'grade', 'comments', 'rating', 'session', 'owner' ]

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = [ 'label', 'weight' ]

class UserSerializer(serializers.ModelSerializer):
    user_sessions = serializers.PrimaryKeyRelatedField(many=True, queryset=Session.objects.all())
    user_climbs = serializers.PrimaryKeyRelatedField(many=True, queryset=Climb.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'user_sessions', 'user_climbs']
