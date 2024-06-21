from django.shortcuts import render
from slots.models import Slots
from turf.models import Turf

# Create your views here.


def avwslots(request):
    obj=Slots.objects.all()
    context={
        'b':obj
    }
    return render(request,'slots/aviewslotes.html',context)


def add_slot(request):
    ss=request.session["u_id"]
    obb=Turf.objects.filter(manager_id=ss)
    context={
        'y':obb
    }
    if request.method=="POST":
        obj=Slots()
        obj.turf_id=request.POST.get('tn')
        obj.start_time=request.POST.get('sst')
        obj.end_time=request.POST.get('set')
        obj.price=request.POST.get('sprice')
        obj.status="pending"
        obj.save()
        return mngeslot(request)
    return render(request, 'slots/slot.html',context)

def remove(request,idd):
    obj=Slots.objects.get(slot_id=idd)
    obj.delete()
    return mngeslot(request)



def slot(request):
    obk=""
    ss=request.session["u_id"]
    obb = Turf.objects.filter(manager_id=ss)
    if request.method=="POST":
        obj=Slots()
        obj.turf_id=request.POST.get('tn')
        obj.start_time=request.POST.get('sst')
        obj.end_time=request.POST.get('set')
        obj.price=request.POST.get('sprice')
        obj.status="pending"
        obj.save()
        obk = "success"
    context = {
        'y': obb,
        'msg':obk
    }
    return render(request,'slots/slot.html',context)


def uvwslot(request):
    obj=Slots.objects.all()
    context={
        'a':obj
    }
    return render(request,'slots/uviewslot.html',context)


def mngeslot(request):
    ss=request.session["u_id"]
    obj=Slots.objects.filter(turf__manager_id=ss)
    context={
        'a':obj
    }
    return render(request,'slots/manageslot.html',context)

from django.db.models import Q

def uvwbookturf(request):
    if request.method=='POST':
        vv=request.POST.get('search')
        sv=request.POST.get('sea')
        obj = Slots.objects.filter(Q(start_time=vv) | Q(turf__location__icontains=vv))
        context={
            'c':obj
        }
        return render(request,'slots/uviewbookturf.html',context)
    else:
        obj=Slots.objects.exclude(status='Booked')
        context={
            'c':obj
        }
    return render(request, 'slots/uviewbookturf.html', context)


