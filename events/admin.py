from django.contrib import admin


from .models import Match, Event

# Register your models here.
admin.site.register(Match)
admin.site.register(Event)
