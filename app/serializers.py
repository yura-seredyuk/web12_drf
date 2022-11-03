from django.contrib.auth.models import User, Group
from .models import Address, UserList
from rest_framework import serializers
from .validator import AddressValidator


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
        validators = [AddressValidator()]

    def create(self, validated_data):
        address = Address.objects.filter(**validated_data)
        if address:
            raise serializers.ValidationError("Serializer error: Address with tis data is already exists.")
        rezults = Address.objects.create(**validated_data)
        return rezults

    def update(self, instance, validated_data):
        address = Address.objects.filter(**validated_data).first()
        if address:
            if address == instance:
                return instance
            else:
                raise serializers.ValidationError("Serializer error: Address with tis data is already exists.")
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.street = validated_data.get('street', instance.street)
        instance.house_num = validated_data.get('house_num', instance.house_num)
        instance.appartaments = validated_data.get('appartaments', instance.appartaments)
        instance.save()
        return instance

class UsersListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserList
        fields = ['id', 'username', 'email', 'address']
