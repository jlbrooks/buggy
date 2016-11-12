from django.db import models

class Pusher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def name(self):
        return ' '.join([self.first_name, self.last_name])