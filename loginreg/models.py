from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    sapid=models.CharField(blank=True,null=True,max_length=11,unique=True,default=None)
    committee=models.CharField(blank=True,null=True,max_length=50,unique=True,default=None)
    college=models.CharField(blank=True,null=True,max_length=100,default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_committee = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin