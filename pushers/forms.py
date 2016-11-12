from django.forms import ModelForm
from pushers.models import Pusher


class PusherForm(ModelForm):
    class Meta:
        model = Pusher
        fields = ['first_name', 'last_name', 'phone']