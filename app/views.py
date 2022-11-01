from django.contrib.auth.models import User, Group
from .models import Address, UserList
from rest_framework import viewsets, permissions, status
from .serializers import UserSerializer, GroupSerializer,\
                AddressSerializer, UsersListSerializer 
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows address to be viewed or edited.
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UsersListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows userl list to be viewed or edited.
    """
    queryset = UserList.objects.all()
    serializer_class = UsersListSerializer


class AddressView:
    class AddressList(APIView):
        def get(self, request, format=None):
            address = Address.objects.all()
            serializer = AddressSerializer(address, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = AddressSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class Address(APIView):
        def get_object(self, pk):
            try:
                return Address.objects.get(pk=pk)
            except Address.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            address = self.get_object(pk)
            serializer = AddressSerializer(address)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            data = request.data
            address = self.get_object(pk)
            serializer = AddressSerializer(address, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            address = self.get_object(pk)
            address.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)