from django.db import models

class Pusher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def name(self):
        return ' '.join([self.first_name, self.last_name])

    def __str__(self):
        return self.name()

class Buggy(models.Model):
    name = models.CharField(max_length=50)

    @classmethod
    def choices(cls):
        return [(b.id, b.name) for b in cls.objects.all()]

class RollsDay(models.Model):
    date = models.DateField()
    active_pushers = models.ManyToManyField(Pusher)

class Roll(models.Model):
    day = models.ForeignKey(RollsDay)

class BuggyRoll(models.Model):
    buggy = models.ForeignKey(Buggy)
    roll = models.ForeignKey(Roll)

    def hills(self):
        return self.rollhill_set.all().order_by('hill')

class RollHill(models.Model):
    roll = models.ForeignKey(BuggyRoll)
    pusher = models.ForeignKey(Pusher)
    hill = models.PositiveIntegerField()