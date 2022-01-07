from django.contrib import admin

from .models import Meetup, Location, Participant


class MeetAdmin(admin.ModelAdmin):
  list_display = ('title', 'date', 'location')
  list_filter = ('location', 'date')
  #everytime ppl type the title ,automatic add the same to slug
  prepopulated_fields = {'slug': ('title', )}

admin.site.register(Meetup, MeetAdmin)  
admin.site.register(Location)
admin.site.register(Participant)