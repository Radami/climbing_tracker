import datetime
import calendar

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Session, Climb, Grade

# Create your tests here.
class SessionModelTests(TestCase):

    def test_recent_with_future_date(self):
        """ was_recorded_recently() returns False for sessions whose date is in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        future_session = Session(date=time)
        self.assertIs(future_session.was_recorded_recently(), False)

    def test_recent_with_old_date(self):
        """ was_recorded_recently() returns False for sessions older than 5 days"""
        time = timezone.now() - datetime.timedelta(days=30)
        future_session = Session(date=time)
        self.assertIs(future_session.was_recorded_recently(), False)

    def test_recent_with_recent_date(self):
        """ was_recorded_recently() returns True for sessions recorded within last 5 days"""
        time = timezone.now() - datetime.timedelta(days=4)
        future_session = Session(date=time)
        self.assertIs(future_session.was_recorded_recently(), True)


def create_session(center, time=timezone.now() - datetime.timedelta(3), rating=12345):
    """
    Create a session for that center, days offset in the past from now
    """
    return Session.objects.create(center=center, date=time)

class SessionIndexViewTests(TestCase):
    def test_no_session(self):
        """
        If no sessions exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('journal:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No sessions are available")

    def test_past_session(self):
        """
        Sessions with a date in the past are displayed on the index page
        """
        time = timezone.now() - datetime.timedelta(3)
        create_session("Castle", time)
        response = self.client.get(reverse('journal:index'))
        self.assertQuerysetEqual(
            response.context['latest_sessions'], 
            ['<Session: Castle on ' + str(time) + '>']
        )

class SessionDetailViewTests(TestCase):
    def test_session(self):
        """
        Test a session displays all the relevant fields
        """
        time = timezone.now() - datetime.timedelta(3)
        time_str = str(time.day) + " " + str(calendar.month_name[time.month][:3]) + " " + str(time.year)
        session = create_session('Test center', time)
        grade = Grade.objects.create(label='1A', weight = 5)
        climb = Climb.objects.create(grade=grade, comments="Test climb", session=session)

        response = self.client.get(reverse('journal:detail', args=(session.id,)))
        self.assertContains(response, session.center)

        self.assertContains(response, time_str)

        self.assertContains(response, '1A - Test climb')
        