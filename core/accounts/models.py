from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AccountOwner(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)