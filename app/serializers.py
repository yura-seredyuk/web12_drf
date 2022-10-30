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


class UsersListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserList
        fields = ['id', 'username', 'email', 'address']
