from enum import Enum
from django.db import models

# Create your models here.



class ROLE(Enum):
    ADMIN = "admin"
    REGULAR = "regular"

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]

class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=10, choices=ROLE.choices(), default=ROLE.REGULAR.value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"