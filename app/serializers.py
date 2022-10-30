from django.contrib.auth.models import User, Group
from .models import Address, UserList
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'country', 'city', 'zip_code', 'street', 'house_num', 'appartaments']

    def create(self, validated_data):
        # print(validated_data)
        rezults = Address.objects.create(**validated_data)
        # print(rezults.id)
        return rezults

    def update(self, instance, validated_data):
        pass


class UsersListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserList
        fields = ['id', 'username', 'email', 'address']
