from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.first_name, self.last_name, self.phone, self.email)