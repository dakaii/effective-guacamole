from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.accounts.models.abstracts import TimeRecordMixin

class AccountOwnerManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create a user with the given email and password."""
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular user with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a super user with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class AccountOwner(AbstractUser, TimeRecordMixin):
    # username = None
    date_joined = None
    email = models.EmailField(_('email address'), unique=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False)


    objects = AccountOwnerManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.__class__.__name__} {self.email}'
