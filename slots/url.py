from django.conf.urls import url
from slots import views

urlpatterns=[
    url('avwslots/',views.avwslots),
    url('mngslots/',views.mngeslot),
    url('remove/(?P<idd>\w+)',views.remove),
    url('slot/',views.slot),
    url('s/',views.uvwslot),
    url('add/', views.add_slot),
    url('uvwbooktf/', views.uvwbookturf),

]