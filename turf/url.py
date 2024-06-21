from django.conf.urls import url
from turf import views

urlpatterns=[
    url('addtf/',views.aturf),
    url('upturf/(?P<idd>\w+)',views.udturf),
    url('delete/(?P<idd>\w+)',views.delete),
    url('uvwturf/',views.uvwturf),
    url('vwturf/',views.vwturf),
    url('vwupdturf/',views.vwupdturf),



]