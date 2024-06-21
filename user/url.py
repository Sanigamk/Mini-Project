from django.conf.urls import url
from user import views

urlpatterns=[
    url('pfedit/(?P<idd>\w+)',views.prfledit),
    url('delete/(?P<idd>\w+)',views.delete),
    url('usr/',views.user),
    url('uvwupdtpf/',views.uvwupdtpf),

]