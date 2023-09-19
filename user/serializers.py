from rest_framework import serializers
from user.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
