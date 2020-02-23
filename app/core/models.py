from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUser, \
                                       PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """ Create and saves a new user """
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
        
# class User(AbstractBaseUser, PermissionsMixin):
    