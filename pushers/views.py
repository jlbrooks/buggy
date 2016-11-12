from django.shortcuts import render, redirect
from pushers.models import *
from pushers.forms import PusherForm

def index(request):
    context = {
        'pushers': Pusher.objects.all()
    }
    return render(request, "index.html", context)

def create_pusher(request):
    if request.method == 'POST':
        form = PusherForm(request.POST)
        if form.is_valid():
            p = Pusher(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'])

            p.save()

    return redirect(index)