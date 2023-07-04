import datetime

from django.db import models
from django.utils import timezone

class Grade(models.Model):
    label = models.CharField(max_length=10)
    weight = models.IntegerField()

    def __str__(self):
        return self.label

class Location(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='user_location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' by ' + str(self.owner)

class Session(models.Model):
    location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    date = models.DateTimeField('date of climb')
    rating = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='user_sessions',on_delete=models.CASCADE)

    def was_recorded_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.date <= now

    def __str__(self):
        return self.location.name + " on " + str(self.date.date())

class SessionPartner(models.Model):
    session = models.ForeignKey(Session, related_name="partners", on_delete=models.CASCADE)
    displayName = models.CharField(max_length=50)

class Climb(models.Model):
    grade =  models.ForeignKey(Grade, on_delete=models.CASCADE)
    comments = models.CharField(max_length=250, default=None)
    rating = models.IntegerField(default=0)
    session = models.ForeignKey(Session, related_name='climbs', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='user_climbs',on_delete=models.CASCADE)
    climb_type = models.CharField(max_length=20, default="Flash")
    takes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.grade) + " - " + self.comments + " : " + str(self.rating)
    

