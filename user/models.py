from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length=100)
    standard = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    history = HistoricalRecords()

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return self.choice_text
