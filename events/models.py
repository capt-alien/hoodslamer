from django.db import models
from wrestlers.models import Wrestler
# Create your models here.



class Match(models.Model):
    """This is the model for the individual matches, where one or more
        wrestler wrestle in the ring."""
    date = models.DateField()
    wrestlers = models.ManyToManyField(Wrestler)
    summary = models.CharField(max_length=200, blank=True, null=True)
    outcome = models.CharField(max_length=200, blank=True, null=True)
    winners = models.ManyToManyField(Wrestler, blank=True, related_name="winners") #,choices=wrestlers)
    losers = models.ManyToManyField(Wrestler, blank=True, related_name="losers") #,choices=wrestlers)


class Event(models.Model):
    """Model for the events. Should be connected to a few matches"""
    LEAUGES = (
        ('HS', 'Hoodslam'),
        ('GLAM', 'Guilty Leathal Action Mayham'),
        ('SGTWS', 'Sexy Good Time Wresleing Show')
                )
    title = models.CharField(max_length=60)
    leauge = models.CharField(max_length=5, choices=LEAUGES, default='HS')
    date = models.DateField()
    matches = models.ManyToManyField(Match, blank=True, related_name="matches")
    location = models.CharField(max_length=200, default='Oakland Metro Oprah House')
