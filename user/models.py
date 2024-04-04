from django.db import models
from django.contrib.auth.models import AbstractUser


# Способ расширения модели пользователя через наследование
class Users(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.username

# Способ расширения модели пользователя через OneToOneField
# class Profile(models.Model):
#     user = models.OneToOneField(Users, on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
#     age = models.PositiveIntegerField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username

