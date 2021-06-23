from django.db import IntegrityError
from rest_framework import serializers

from .models import AccountOwner


class AccountOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountOwner
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff',
                  'is_active', 'date_joined')
