from django.forms import ModelForm
from pushers.models import *


class PusherForm(ModelForm):
    class Meta:
        model = Pusher
        fields = ['first_name', 'last_name', 'phone']

class BuggyForm(ModelForm):
    class Meta:
        model = Buggy
        fields = ['name']

class RollsDayForm(ModelForm):
    class Meta:
        model = RollsDay
        fields = ['date']