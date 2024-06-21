from django.conf.urls import url
from manager import views

urlpatterns=[
    url('managemngr/',views.mmangr),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject),
    url('mngr/',views.mangr),
    url('mupdtpf/(?P<idd>\w+)',views.mupdatepl),
    url('vwupdtmnr/',views.vwupdmngr),
    url('delete/(?P<idd>\w+)',views.delete)
]