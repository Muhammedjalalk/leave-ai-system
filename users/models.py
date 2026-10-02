from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        EMPLOYEE='EMPLOYEE','Employee',
        MANAGER='MANAGER', 'Manager',
        HR='HR','HR'

    role=models.CharField(max_length=10,choices=Role.choices,default=Role.EMPLOYEE)
    department=models.CharField(max_length=100,blank=True)
    manager=models.ForeignKey('self',null=True,on_delete=models.SET_NULL,related_name='team')

    def __str__(self):
        return f"{self.username}({self.role})"


