from rest_framework import serializers

from apps.transactions.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('from_user', 'to_user', 'amount', 'created')

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)