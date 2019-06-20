from django.db import models

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
    nickname = models.CharField(max_length=200, null=True)
    affiliation = models.CharField(max_length=200, null=True)
    bio = models.CharField(max_length=1000)
    sex = models.CharField(max_length=2, choices=SEX_TYPES)
    birthdate = models.DateField('birthday', null=True)
    weight = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    loses = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    date = models.DateField()
    # event = models.ForeignKey(Event, on_delete=models.CASCADE)
    wrestlers = models.ManyToManyField(Wrestler)
    summary = models.CharField(max_length=200)
    #eventually we will be able to selelct multiple winners/loosers
    winners = models.CharField(max_length=200, null=True) #,choices=wrestlers)
    loosers = models.CharField(max_length=200, null=True) #,choices=wrestlers)

    # def __str__(self):
    #     return self.wrestlers

    def update_stats(self, winners, losers):
        """This method will automatically go through the
            winners and loosers and update the stats of the
            wrestlers in the db"""
        pass
