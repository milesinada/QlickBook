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
