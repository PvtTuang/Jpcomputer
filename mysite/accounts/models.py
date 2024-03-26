from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    OWNER = 'Owner'
    CUSTOMER = 'Customer'
    ROLE_CHOICES = [
        (OWNER, 'Owner'),
        (CUSTOMER, 'Customer'),
    ]

    name = models.CharField(max_length=100, choices=ROLE_CHOICES, default=CUSTOMER)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username