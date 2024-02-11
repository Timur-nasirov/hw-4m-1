from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'direction', 'balance')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=50,
        write_only=True
    )
    password2 = serializers.CharField(
        max_length=50,
        write_only=True
    )
    class Meta:
        model = User
        fields = ('username', 'phone', 'direction', 'password', 'password2')

def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
        raise serializers.ValidationError({'detail':'Пароли отличаются'})
    if len(attrs['password']) < 8:
        raise serializers.ValidationError({'detail': 'Длина пароля должна быть больше 8 символов'})
    if '+996' not in attrs['phone']:
        raise serializers.ValidationError({'detail':'Неправильный номер телефона (формат: +996 ххх ххх ххх)'})
    return attrs

def create(self, data):
    user = User.objects.create(
        username=data['username'], 
        phone=data['phone'],
        password=data['password'],
        direction=data['direction']
    )
    user.set_password(data['password'])
    user.save()
    return user

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'direction', 'balance')