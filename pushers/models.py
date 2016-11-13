from django.db import models

class Pusher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def name(self):
        return ' '.join([self.first_name, self.last_name])

class Buggy(models.Model):
    name = models.CharField(max_length=50)

class RollsDay(models.Model):
    date = models.DateField()
    active_pushers = models.ManyToManyField(Pusher)