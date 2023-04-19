from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username ,sapid,committee=None,college=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not sapid:
            raise ValueError('Users must have an sapid')

        user = self.model(
            username = username,
            sapid = sapid,
            committee=committee,
            college=college,

        )
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username = username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
