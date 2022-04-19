from rooms.models import Room
from rest_framework import serializers

"id","host","topic","name","description","participants","created","updated"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields= ["id","host","topic","name","description"]
        read_only_fields= ["host"]

class ViewRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields= ["id","host","topic","name","description","created","updated"]