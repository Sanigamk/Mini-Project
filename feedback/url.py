from django.conf.urls import url
from feedback import views

urlpatterns=[
    url('avwfb/',views.avwfb),
    url('feedback/',views.fb),
    url('mvwfb/',views.mvwfb),



]