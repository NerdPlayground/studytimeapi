from topics.models import Topic
from rest_framework import serializers

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model= Topic
        fields= ["id","name"]

class ViewTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model= Topic
        fields= ["id","name"]