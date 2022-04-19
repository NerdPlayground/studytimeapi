from rooms.models import Room
from django.contrib import admin

'''
"id","host","topic","name","description","participants","created","updated"
'''

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display= ["id","host","topic","name","description"]
    search_fields= ["host","topic","name"]
    list_filter= ["host","topic"]