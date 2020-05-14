from rest_framework import serializers
from .models import Room
from users.serializers import UserSerializer


class RoomSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Room
        fields = ("pk", "name", "price", "instant_book", "user")


class SingleRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        exclude = ()