from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    address = models.TextField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user + 'Bill.'
