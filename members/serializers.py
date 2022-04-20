from members.models import Member
from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username= serializers.CharField(max_length=150)
    email= serializers.EmailField(max_length=150)
    password= serializers.CharField(min_length=8,max_length=20,write_only=True)

class EditMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields= ['id','username','first_name','last_name','email']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields= ['id','username','first_name','last_name','email']