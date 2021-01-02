import datetime

from django.db import models
from django.utils import timezone

class Grade(models.Model):
    label = models.CharField(max_length=10)
    weight = models.IntegerField()

    def __str__(self):
        return self.label


class Session(models.Model):
    center = models.CharField(max_length=50)
    date = models.DateTimeField('date of climb')
    rating = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='user_sessions',on_delete=models.CASCADE)

    def was_recorded_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.date <= now

    def __str__(self):
        return self.center + " on " + str(self.date)


class Climb(models.Model):
    grade =  models.ForeignKey(Grade, on_delete=models.CASCADE)
    comments = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)
    session = models.ForeignKey(Session, related_name='climbs', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='user_climbs',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.grade) + " - " + self.comments + " : " + str(self.rating)
