from rest_framework import serializers
from contributions.models import Contribution

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contribution
        fields= ["id","contributor","room","body"]
        read_only_fields= ["contributor"]