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

    def was_recorded_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.center + " on " + str(self.date)


class Climb(models.Model):
    grade =  models.ForeignKey(Grade, on_delete=models.CASCADE)
    comments = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.grade) + " - " + self.comments
