"""buggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pushers import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    # Rolls urls
    url(r'^rolls$', views.rolls, name='rolls'),
    url(r'^create_roll_day$', views.create_roll_day, name='create_roll_day'),
    url(r'^edit_active_pushers/(?P<r_id>[0-9]+)$', views.edit_active_pushers, name='edit_active_pushers'),
    url(r'^activate_pusher/(?P<r_id>[0-9]+)/(?P<p_id>[0-9]+)$', views.activate_pusher, name='activate_pusher'),
    url(r'^deactivate_pusher/(?P<r_id>[0-9]+)/(?P<p_id>[0-9]+)$', views.deactivate_pusher, name='deactivate_pusher'),

    # Pusher urls
    url(r'^pushers$', views.pushers, name='pushers'),
    url(r'^create_pusher$', views.create_pusher, name='create_pusher'),
    url(r'^delete_pusher/(?P<p_id>[0-9]+)$', views.delete_pusher, name='delete_pusher'),
]
