from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from apps.transactions.models import Transaction
from apps.transactions.serializers import TransactionSerializer
from apps.users.models import User

class TransactionsAPIViews(GenericViewSet, 
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_permissions(self):
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), )
        return (AllowAny(), )
    
    def perform_create(self, serializer):
        try:
            from_user = get_object_or_404(User, username=str(serializer.validated_data['from_user']))
            to_user = get_object_or_404(User, username=str(serializer.validated_data['to_user']))
            amount = float(serializer.validated_data['amount'])

            if amount > float(from_user.balance):
                return Response({'detail':'Недостаточно средств для перевода'}, status=status.HTTP_400_BAD_REQUEST)

            from_user.balance -= amount
            to_user.balance += amount

            from_user.save()
            to_user.save()

            transfer = Transaction(from_user=from_user, to_user=to_user, amount=amount)
            transfer.save()

        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'detail': 'Неправильный формат'}, status=status.HTTP_400_BAD_REQUEST)