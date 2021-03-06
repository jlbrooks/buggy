from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from pushers.models import *
from pushers.forms import *
import random

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(rolls)


    return render(request, "login.html")

@login_required
def pushers(request):
    context = {
        'pushers': Pusher.objects.all()
    }
    return render(request, "pushers.html", context)

@login_required
def rolls(request):
    context = {
        'rollsDays': RollsDay.objects.all()
    }
    return render(request, "rolls.html", context)

@login_required
def create_roll_day(request):
    if request.method == 'POST':
        form = RollsDayForm(request.POST)
        if form.is_valid():
            r = RollsDay(date=form.cleaned_data['date'])
            r.save()

    return redirect(rolls)

@login_required
def edit_active_pushers(request, r_id):
    roll = get_object_or_404(RollsDay, id=r_id)
    active = roll.active_pushers.all()
    context = {
        'roll': roll,
        'active_pushers': active,
        'inactive_pushers': Pusher.objects.exclude(id__in=active)
    }
    return render(request, "edit_active_pushers.html", context)

@login_required
def activate_pusher(request, r_id, p_id):
    roll = get_object_or_404(RollsDay, id=r_id)
    pusher = get_object_or_404(Pusher, id=p_id)

    roll.active_pushers.add(pusher)

    return redirect(edit_active_pushers, r_id)

@login_required
def deactivate_pusher(request, r_id, p_id):
    roll = get_object_or_404(RollsDay, id=r_id)
    pusher = get_object_or_404(Pusher, id=p_id)

    roll.active_pushers.remove(pusher)

    return redirect(edit_active_pushers, r_id)

@login_required
def edit_roll(request, r_id):
    roll = get_object_or_404(Roll, id=r_id)
    context = {
        'roll': roll
    }

    if request.method == 'POST':
        if 'regenerate' in request.POST:
            roll.assign_pushers(roll.buggies)
        else:
            assignments = [k for k in request.POST.keys() if k[0:5] == 'hill-']
            for assign in assignments:
                pusher = get_object_or_404(Pusher, id=request.POST[assign])
                hill = get_object_or_404(RollHill, id=assign[5])
                hill.pusher = pusher
                hill.save()


    return render(request, "edit_roll.html", context)

@login_required
def create_roll(request, r_id):
    rollsDay = get_object_or_404(RollsDay, id=r_id)
    context = {
        'rollsDay': rollsDay,
        'buggies': Buggy.objects.all()
    }

    if request.method == 'POST':
        form = RollForm(request.POST)
        if form.is_valid():
            # Generate the roll
            buggies = [Buggy.objects.get(id=i) for i in form.cleaned_data['buggies']]
            roll = Roll(day=rollsDay)
            roll.save()

            roll.assign_pushers(buggies)

            return redirect(edit_roll, roll.id)

    return render(request, "create_roll.html", context) 

@login_required
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

@login_required
def delete_pusher(request, p_id):
    pusher = get_object_or_404(Pusher, id=p_id)
    pusher.delete()
    return redirect(pushers)

@login_required
def buggies(request):
    context = {
        'buggies': Buggy.objects.all()
    }
    return render(request, "buggies.html", context)

@login_required
def create_buggy(request):
    if request.method == 'POST':
        form = BuggyForm(request.POST)
        if form.is_valid():
            b = Buggy(name=form.cleaned_data['name'])
            b.save()

    return redirect(buggies)

@login_required
def delete_buggy(request, b_id):
    buggy = get_object_or_404(Buggy, id=b_id)
    buggy.delete()
    return redirect(buggies)