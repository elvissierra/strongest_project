from rest_framework import serializers
from .models import Mon


class ObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mon
        fields = "__all__"
