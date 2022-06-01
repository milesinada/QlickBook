# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class Status(models.Model):
#     description = models.CharField(max_length=96)

#     def __str__(self):
#         return self.description

# class CustomUser(AbstractUser):
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     email = models.EmailField(blank=True)
#     phone = models.PositiveIntegerField(null=True, blank=True)
#     status = models.ForeignKey(
#         Status,
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True
#     )
#     is_active = models.BooleanField()


from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser
                                        )


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  # superuser
    objects = BaseUserManager()

    USERNAME_FIELD = 'email'  # username
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    def is_admin(self):
        "Is the user an admin member?"
        return self.admin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
