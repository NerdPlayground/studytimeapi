from members.models import Member
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields= ['id','username','email','password']
        read_only_fields = ['password']

class EditMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields= ['id','username','first_name','last_name','email']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= Member
        fields= ['id','username','first_name','last_name','email']