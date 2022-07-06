from django.urls import re_path
from . import views

app_name = 'music'
urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^(?P<album_id>[0-9]+)$', views.detail, name='detail'),
    re_path(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]
