import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Event, Match

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_event(self):
        """
        was_published_recently() returns False for events whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_event = Event(date=time)
        self.assertIs(future_event.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Event(date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Event(date=time)
        self.assertIs(recent_question.was_published_recently(), True)

#
#
# # Create your tests here.
# class Test_Event_Class(TestCase):
#
#     def test_get_event():
#         """create new event"""
#         pass
#
#     def test_default_location():
#         # assert testEvent.location == 'Oakland Metro Oprah House'
#         # assert testEvent.loaction != 'Berkley'
#         pass
#
#     def test_delete_event():
#         pass
#
#
# class Test_Match_Class(TestCase):
#     def test_create_match():
#         pass
#
#     def test_no_default_win():
#         pass
#
#     def test_no_default_loss():
#         pass
