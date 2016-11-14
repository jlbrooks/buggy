from django.db import models
from django.core.exceptions import ObjectDoesNotExist
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
        # First, generate/retrieve the rolls for each buggy
        bRolls = [BuggyRoll.objects.get_or_create(buggy=b, roll=self)[0] for b in buggies]
        # Build all of the hill objects
        hills = []
        for bRoll in bRolls:
            for i in range(2,6):
                try:
                    hill = RollHill.objects.get(roll=bRoll,hill=i)
                except RollHill.DoesNotExist:
                    hill= RollHill(roll=bRoll,hill=i)
                hills.append(hill)

        # If we can't do it with 2-5's then don't try
        if len(pushers) + len(buggies) < len(hills):
            return "Not enough pushers - need %d" % len(hills) - len(buggies)

        # Assign 2-5's
        while len(pushers) < len(hills):
            hill_2 = [h for h in hills if h.hill == 2][0]
            hill_5 = [h for h in hills if h.hill == 5][0]
            pusher = pushers.pop()
            hill_2.pusher = pusher
            hill_5.pusher = pusher
            hills.remove(hill_2)
            hills.remove(hill_5)

            hill_2.save()
            hill_5.save()
        
        # Assign rest of pushers to hills 
        while len(hills) > 0:
            hill = hills.pop()
            hill.pusher = pushers.pop()
            hill.save()

        return None

class BuggyRoll(models.Model):
    buggy = models.ForeignKey(Buggy)
    roll = models.ForeignKey(Roll)

    def hills(self):
        return self.rollhill_set.all().order_by('hill')

class RollHill(models.Model):
    roll = models.ForeignKey(BuggyRoll)
    pusher = models.ForeignKey(Pusher)
    hill = models.PositiveIntegerField()