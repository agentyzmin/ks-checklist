from django.db import models
from django.contrib.auth.models import User

class Apartment(models.Model):
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    ap_class = models.IntegerField()
    state = models.CharField(max_length=30)
    developer_offer = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Question(models.Model):
    apartment = models.ManyToManyField(Apartment)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ManyToManyField(User)
    apartment = models.ForeignKey(Apartment)
    question = models.ForeignKey(Question)
    choice = models.IntegerField(default=2)

    def __str__(self):
        return str(self.choice)

