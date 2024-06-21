from django.conf.urls import url
from temp import views
urlpatterns=[
    url('home/', views.home),
    url('admin/',views.admin),
    url('manager/',views.manager),
    url('user/',views.user),
    url('mh/', views.main_home),
    url('mu/', views.main_user),
    url('ma/', views.main_admin),
    url('mm/', views.main_manager)
]