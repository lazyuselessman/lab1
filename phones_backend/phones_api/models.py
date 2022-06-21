from django.contrib.auth.models import User
from django.db import models


class Phone(models.Model):
    surname = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.surname.username} Phone'

class Number(models.Model):
    phone = models.ForeignKey(Phone, related_name='numbers', on_delete=models.CASCADE)
    number_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.phone.surname.username} Phone: {self.number_text}'
