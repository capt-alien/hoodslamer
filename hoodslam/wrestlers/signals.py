# from django.db.models.signals import post_save
#
#
# def update_stats(Match):
#     """This method will automatically go through the
#         winners and loosers and update the stats of the
#         wrestlers in the db"""
#     for winner in Match.winners:
#         #find object in db
#         new_win = Wrestler.objects.filter(name=winner)
#         #update wins
#         new_win.wins += 1
#         new_win.save()
#     for loser in Match.loosers:
#         #find object in db
#         new_loss = Wrestler.objects.filter(name=loser)
#         #update wins
#         new_loss.losses += 1
#         new_loss.save()
#     return {'message': "Wins/losses recorded"}
