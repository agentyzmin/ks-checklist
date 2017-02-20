from django.db import models


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
    apartment = models.ForeignKey(Apartment)
    question = models.ForeignKey(Question)
    choice_text = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

