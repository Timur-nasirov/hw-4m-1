from rest_framework import serializers
from apps.users.models import User 

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'balance', )
