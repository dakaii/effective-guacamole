from core.accounts.controllers.social_signup import SocialSignUp
from django.urls import path

urlpatterns = [
    path('social/google/', SocialSignUp.as_view(), name='social-google'),
]
