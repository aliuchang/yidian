from rest_framework.serializers import ModelSerializer
from .models import  UserInfo,Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class UserInfoSerializer(ModelSerializer):
    addrs = AddressSerializer(many=True)
    class Meta:
        model = UserInfo
        fields = '__all__'
