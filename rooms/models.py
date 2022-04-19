import uuid
from django.db import models

class Room(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    host= models.ForeignKey(
        'members.Member',
        related_name='rooms',
        on_delete=models.CASCADE
    )
    topic= models.ForeignKey(
        'topics.Topic',
        related_name='rooms',
        on_delete=models.CASCADE
    )
    name= models.CharField(max_length=255)
    description= models.TextField(null=True,blank=True)
    participants= models.ManyToManyField('members.Member')
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)