from django import forms
from pushers.models import *


class PusherForm(forms.ModelForm):
    class Meta:
        model = Pusher
        fields = ['first_name', 'last_name', 'phone']

class BuggyForm(forms.ModelForm):
    class Meta:
        model = Buggy
        fields = ['name']

class RollsDayForm(forms.ModelForm):
    class Meta:
        model = RollsDay
        fields = ['date']

class RollForm(forms.Form):
    buggies = forms.MultipleChoiceField(choices=Buggy.choices)