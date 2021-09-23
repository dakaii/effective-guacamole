# import uuid

from django.contrib.auth import get_user_model
from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework import generics, permissions, status, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from core.accounts.serializers.users import AccountOwnerSerializer

AccountOwner = get_user_model()

CLIENT_ID = ''


class SocialSignUp(generics.CreateAPIView):

    serializer_class = AccountOwnerSerializer
    permission_classes = (permissions.AllowAny,)

    def _google_auth(self, auth_info):
        token = auth_info['id_token']
        idinfo = id_token.verify_oauth2_token(token, requests.Request(),
                                              CLIENT_ID)
        if idinfo['aud'] not in [CLIENT_ID]:
            raise ValueError('Could not verify audience.')
        return idinfo['email']

    def create(self, request, *args, **kwargs):
        login_type = request.data.get('idp_id')
        if login_type == 'google':
            email = self._google_auth(request.data)

        if not AccountOwner.objects.filter(email=email).exists():
            serializer = self.serializer_class(data={
                'email': email,
                # 'password': uuid.uuid4().hex
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()
        token, _ = Token.objects.get_or_create(user__email=email)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
