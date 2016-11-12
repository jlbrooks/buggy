from django.shortcuts import render, redirect, get_object_or_404
from pushers.models import *
from pushers.forms import PusherForm

def index(request):
    context = {
        'pushers': Pusher.objects.all()
    }
    return render(request, "index.html", context)

def pushers(request):
    context = {
        'pushers': Pusher.objects.all()
    }
    return render(request, "pushers.html", context)

def create_pusher(request):
    if request.method == 'POST':
        form = PusherForm(request.POST)
        if form.is_valid():
            p = Pusher(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'])

            p.save()

    return redirect(pushers)

def delete_pusher(request, p_id):
    pusher = get_object_or_404(Pusher, id=p_id)
    pusher.delete()
    return redirect(pushers)