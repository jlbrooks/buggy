from django.db import models
import random

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

    class Meta:
        ordering = ['-date']

class Roll(models.Model):
    day = models.ForeignKey(RollsDay)

    @property
    def buggies(self):
        return list(set([r.buggy for r in BuggyRoll.objects.filter(roll=self)]))

    @property
    def pushers(self):
        return list(self.day.active_pushers.all())

    def assign_pushers(self, buggies):
        pushers = self.pushers
        # Shuffle the list of pushers
        random.shuffle(pushers)
        cur_pusher = 0
        
        for buggy in buggies:
            bRoll,_ = BuggyRoll.objects.get_or_create(buggy=buggy, roll=self)
            bRoll.save()
            for i in range(2,6):
                hill,_ = RollHill.objects.get_or_create(roll=bRoll,hill=i,pusher=pushers[cur_pusher])
                cur_pusher = cur_pusher + 1
                # If we wrap, re-shuffle and start over
                if cur_pusher >= len(pushers):
                    random.shuffle(pushers)
                    cur_pusher = 0
                hill.save()

class BuggyRoll(models.Model):
    buggy = models.ForeignKey(Buggy)
    roll = models.ForeignKey(Roll)

    def hills(self):
        return self.rollhill_set.all().order_by('hill')

class RollHill(models.Model):
    roll = models.ForeignKey(BuggyRoll)
    pusher = models.ForeignKey(Pusher)
    hill = models.PositiveIntegerField()