from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Employees(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
