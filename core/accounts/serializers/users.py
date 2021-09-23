from django.db import IntegrityError
from rest_framework import serializers

from core.accounts.models.users import AccountOwner


class AccountOwnerSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=100, min_length=6)
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = AccountOwner
        fields = (
            'id','email', 'password', 'is_staff',
            'is_active', 'date_joined')

    def validate_email(self, value):
        if AccountOwner.objects.filter(email=value).exists():
            raise serializers.ValidationError('The email is already taken.')
        return value

    def create(self, validated_data):
        return AccountOwner.objects.create_user(**validated_data)
