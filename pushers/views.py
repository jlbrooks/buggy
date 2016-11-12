from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def create_pusher(request):
    return index(request)