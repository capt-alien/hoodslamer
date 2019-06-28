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

class Match(models.Model):
    date = models.DateField()
    # event = models.ForeignKey(Event, on_delete=models.CASCADE)
    #Having problems selecting only one wrestler
    wrestlers = models.ManyToManyField(Wrestler)
    summary = models.CharField(max_length=200, blank=True, null=True)
    outcome = models.CharField(max_length=200, blank=True, null=True)
    #eventually we will be able to selelct multiple winners/loosers
    winners = models.ManyToManyField(Wrestler, blank=True, related_name="winners") #,choices=wrestlers)
    losers = models.ManyToManyField(Wrestler, blank=True, related_name="losers") #,choices=wrestlers)
    #post_save -->

def update_stats(sender, instance, created, **kwargs):
    """This method will automatically go through the
        winners and loosers and update the stats of the
        wrestlers in the db"""
    if created:
        print(instance.winners.all())
        for winner in instance.winners.all():
            print(f'winner.name: {winner.name}')
            #find object in db
            new_win = Wrestler.objects.filter(name=winner.name)
            #update wins
            new_win.wins = new_win.wins + 1
            new_win.save()
        for loser in instance.losers.all():
            #find object in db
            new_loss = Wrestler.objects.filter(name=loser.name)
            #update wins
            new_loss.losses = new_loss.losses + 1
            new_loss.save()
        return {'message': "Wins/losses recorded"}


#signal
m2m_changed.connect(update_stats, sender=Match)


#Django signals (when this happens call this just hoook into a function)
# https://docs.djangoproject.com/en/2.2/ref/signals/   django signals post_save
