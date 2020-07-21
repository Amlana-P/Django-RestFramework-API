from rest_framework import serializers
from webapp.models import Users
from webapp.models import csvDb


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields=('Data',)

class csvDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = csvDb
        fields=('DataBase',)