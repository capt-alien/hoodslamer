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
