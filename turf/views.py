from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.shortcuts import render
from turf.models import Turf
from slots.models import Slots
from category.models import Category
from manager.models import Manager

# Create your views here.


def aturf(request):
    ss=request.session["u_id"]
    obk =""
    obb=Category.objects.all()
    if request.method=="POST":
        a=request.POST.get('tnm')
        obv=Turf.objects.filter(Q(turfname=a))
        if len(obv) > 0:
            obk="user exist"
        else:
            obj=Turf()
            obj.category_id=request.POST.get('st')
            obj.manager_id=ss
            obj.turfname=request.POST.get('tnm')
            obj.email=request.POST.get('tmail')
            obj.location=request.POST.get('tloc')
            # obj.image=request.POST.get('timg')
            myfile=request.FILES['timg']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            obj.image=myfile.name
            obj.save()
            obk = "ok"
            # obx="jj"

    context = {
        'y': obb,
        'msg':obk,
        # 'hi':obx
    }
    return render(request,'turf/addturf.html',context)


def udturf(request,idd):
    ss=request.session["u_id"]
    obb=Turf.objects.get(turf_id=idd)
    obb1=Category.objects.all()
    context={
        'c':obb,
        'xx':obb1
    }
    if request.method=="POST":
        obj=Turf.objects.get(turf_id=idd)
        obj.manager_id=ss
        obj.category_id = request.POST.get('st')
        obj.turfname=request.POST.get('tnm')
        obj.email=request.POST.get('tmail')
        obj.location=request.POST.get('tloc')
        # obj.image=request.POST.get('timg')
        myfile = request.FILES['timg']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
    # try:
    #     myfile=request.FILES['timg']
    #     fs=FileSystemStorage()
    #     filename=fs.save(myfile.name,myfile)
    #     obj.image=myfile.name
    # except:
    #     pass
        obj.save()
        return vwupdturf(request)
    return render(request,'turf/updateturf.html',context)


def delete(request,idd):
    obj=Turf.objects.get(turf_id=idd)
    obj.delete()
    return vwupdturf(request)

def uvwturf(request):
    obj=Turf.objects.all()
    context={
        'a':obj
    }
    return render(request,'turf/uviewturfdetails.html',context)


def vwturf(request):
    obj=Turf.objects.all()
    context={
        'b':obj
    }
    return render(request,'turf/viewturfdetails.html',context)


def vwupdturf(request):
    ss = request.session["u_id"]
    obj=Turf.objects.filter(manager_id=ss)
    context={
        'c':obj
    }
    return render(request,'turf/viewupdateturf.html',context)

