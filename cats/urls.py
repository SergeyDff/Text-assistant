from django.contrib import admin
from django.urls import include, path
from . import views
app_name = 'cat'


urlpatterns = [
    path('', views.index),
    # path('group/<slug:slug>/', include('cat.urls', namespace='cat')),
]
