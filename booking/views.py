from django.shortcuts import render
from booking.models import Booking
from slots.models import Slots
from user.models import User
from category.models import Category
from turf.models import Turf
# Create your views here.

from datetime import datetime


def bookturf(request,idd):
    ss=request.session["u_id"]
    obj1=Slots.objects.get(slot_id=idd)
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d")
    context={
        'xx':obj1,
        'dt': date_time,
    }
    if request.method=='POST':
        obk=""
        obj=Booking()
        obj.date=request.POST.get('td')
        obj.slot_id=idd
        obj.user_id=ss
        # obj.turf_id=1
        obj.status="Booked"
        obj.save()
        obb=Slots.objects.get(slot_id=idd)
        obb.status="Booked"
        obb.save()
    return render(request,'booking/bookturf.html',context)

def mngbooking(request):
    ss=request.session["u_id"]
    obj=Booking.objects.filter(slot__turf__manager_id=ss)
    context={
        'a':obj
    }
    return render(request,'booking/managebooking.html',context)

def accept(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.status='Approved'
    obj.save()
    return mngbooking(request)

def reject(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.status='Rejected'
    obj.save()
    return mngbooking(request)
from payment.models import Payment
def uvwapprdbooking(request):
    ss=request.session["u_id"]
    obj=Booking.objects.filter(status="Approved",user_id=ss)
    context={
        'b':obj,
    }
    return render(request,'booking/uviewapprovedbookingpay.html',context)

def cancel(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.status='canceled'
    obj.save()
    return uvwapprdbooking(request)

def paid(request,idd):
    obj=Booking.objects.get(booking_id=idd)
    obj.pay_status='paid'
    obj.save()
    return uvwapprdbooking(request)

