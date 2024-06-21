from django.conf.urls import url
from payment import views

urlpatterns=[
    url('mvwpay/',views.mvwpay),
    url('payment/(?P<idd>\w+)',views.pay),
    url('bill/(?P<idd>\w+)',views.index)

]