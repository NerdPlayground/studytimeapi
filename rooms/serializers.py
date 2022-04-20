from rooms.models import Room
from rest_framework import serializers

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields= ["id","host","topic","name","description"]
        read_only_fields= ["host"]

class ViewRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields= ["id","host","topic","name","description","created","updated"]