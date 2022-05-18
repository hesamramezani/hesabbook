from rest_framework import serializers
from .models import Expend , Income , User


class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class Expend_serializer(serializers.ModelSerializer):
    class Meta:
        model = Expend
        fields = "__all__"


class Income_serializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"

