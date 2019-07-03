from django.db import models
from django.db.models.signals import m2m_changed

# Create your models here.
class Wrestler(models.Model):
    SEX_TYPES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('D', 'Demon'),
        ('A', 'Angle'),
        ('U', 'Unsure'),
        ('Fl', 'Fluid'),
        ('AS', 'Asexual'),
    )
    name = models.CharField(max_length=60)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    affiliation = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=1000)
    sex = models.CharField(max_length=2, choices=SEX_TYPES)
    birthdate = models.DateField('birthday', blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True, default=0)
    losses = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name
