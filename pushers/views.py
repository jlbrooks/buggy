from django.shortcuts import render, redirect, get_object_or_404
from pushers.models import *
from pushers.forms import *

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

def rolls(request):
    context = {
        'rollsDays': RollsDay.objects.all()
    }
    return render(request, "rolls.html", context)

def create_roll_day(request):
    if request.method == 'POST':
        form = RollsDayForm(request.POST)
        if form.is_valid():
            r = RollsDay(date=form.cleaned_data['date'])
            r.save()

    return redirect(rolls)

def edit_active_pushers(request, r_id):
    roll = get_object_or_404(RollsDay, id=r_id)
    active = roll.active_pushers.all()
    context = {
        'roll': roll,
        'active_pushers': active,
        'inactive_pushers': Pusher.objects.exclude(id__in=active)
    }
    return render(request, "edit_active_pushers.html", context)

def activate_pusher(request, r_id, p_id):
    roll = get_object_or_404(RollsDay, id=r_id)
    pusher = get_object_or_404(Pusher, id=p_id)

    roll.active_pushers.add(pusher)

    return redirect(edit_active_pushers, r_id)

def deactivate_pusher(request, r_id, p_id):
    roll = get_object_or_404(RollsDay, id=r_id)
    pusher = get_object_or_404(Pusher, id=p_id)

    roll.active_pushers.remove(pusher)

    return redirect(edit_active_pushers, r_id)

def create_roll(request, r_id):
    rollDay = get_object_or_404(RollsDay, id=r_id)
    context = {
        'rollDay': rollDay
    }

    if request.method == 'GET':
        return render(request, "create_roll.html", context)

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

def buggies(request):
    context = {
        'buggies': Buggy.objects.all()
    }
    return render(request, "buggies.html", context)

def create_buggy(request):
    if request.method == 'POST':
        form = BuggyForm(request.POST)
        if form.is_valid():
            b = Buggy(name=form.cleaned_data['name'])
            b.save()

    return redirect(buggies)

def delete_buggy(request, b_id):
    buggy = get_object_or_404(Buggy, id=b_id)
    buggy.delete()
    return redirect(buggies)