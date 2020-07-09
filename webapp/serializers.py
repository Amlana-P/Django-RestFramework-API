from rest_framework import serializers
from webapp.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=('Data',)