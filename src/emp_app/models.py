from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Employee(models.Model):

    fullname = models.CharField(max_length=256)
    emp_code = models.CharField(max_length=10)
    email_address = models.EmailField(null=True)
    phone_number = models.CharField(max_length=13)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    address = models.CharField(default='', max_length=512)

    def __str__(self):
        return self.fullname
