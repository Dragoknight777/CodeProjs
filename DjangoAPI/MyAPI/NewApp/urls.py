from django.urls import re_path
from NewApp import views

urlpatterns=[
    re_path(r'^game$', views.developerApi),
    re_path(r'^game/([0-9]+)$', views.developerApi)
]