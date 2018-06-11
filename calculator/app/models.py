from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Calculator(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    operand_one = models.IntegerField()
    operand_two = models.IntegerField()
    operator = models.CharField(max_length=3)
    result = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
