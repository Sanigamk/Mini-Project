from django.conf.urls import url
from booking import views

urlpatterns=[
    url('bookturf/(?P<idd>\w+)',views.bookturf,name='bk'),
    url('mngbooking/',views.mngbooking),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),
    url('uvwapprdbookng/',views.uvwapprdbooking),
    url('can/(?P<idd>\w+)',views.cancel),
    url('paid/(?P<idd>\+)',views.paid)



]