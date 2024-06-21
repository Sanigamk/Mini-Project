from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from manager.models import Manager
from login.models import Login
from django.db.models import Q
# Create your views here.

def mmangr(request):
    obj=Manager.objects.all()
    context={
        'a':obj
    }
    return render(request,'manager/managemanager.html',context)

def accept(request,idd):
    obj=Manager.objects.get(manager_id=idd)
    obj.status="Accepted"
    obj.save()

    obb = Login()
    obb.email = obj.email
    obb.password = obj.password
    obb.u_id = obj.manager_id
    obb.type="manager"
    obb.save()
    return mmangr(request)

def reject(request,idd):
    obj=Manager.objects.get(manager_id=idd)
    obj.status="Rejected"
    obj.save()

    ulog=Login.objects.filter(u_id=idd)
    if len(ulog)>0:
        ulog[0].delete()
    return mmangr(request)

def mangr(request):
    obk=""
    if request.method=="POST":
        # a = request.POST.get('mcon')
        b = request.POST.get('mcmail')
        obv = Manager.objects.filter(Q(email=b))
        if len(obv) > 0:
            obk = "Manager exist"
        else:
            obj=Manager()
            obj.company_name=request.POST.get('mcn')
            obj.name=request.POST.get('mnm')
            obj.liscence_no=request.POST.get('mln')
            # obj.proof=request.POST.get('mpf')
            myfile = request.FILES['mpf']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            obj.proof=myfile.name
            obj.email=request.POST.get('mcmail')
            obj.location=request.POST.get('mloc')
            obj.contact=request.POST.get('mcon')
            obj.password=request.POST.get('mpsw')
            obj.status="pending"
            obj.save()
            obk = "success"
    context = {
        'msg':obk
    }

    return render(request,'manager/manager.html',context)


def mupdatepl(request,idd):
    obb=Manager.objects.get(manager_id=idd)
    context={
        'b':obb
    }
    if request.method=="POST":
        obj=Manager.objects.get(manager_id=idd)
        obj.company_name=request.POST.get('mcn')
        obj.name=request.POST.get('mnm')
        obj.liscence_no=request.POST.get('mln')
        # obj.proof=request.POST.get('mpf')
        myfile=request.FILES['mpf']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        obj.proof=myfile.name
        obj.email=request.POST.get('mcmail')
        obj.location=request.POST.get('mloc')
        obj.contact=request.POST.get('mcon')
        obj.password=request.POST.get('mpsw')
        # obj.status='Accepted'
        obj.save()

        obb = Login.objects.get(u_id=request.session['u_id'], type='manager')
        obb.email = obj.email
        obb.password = obj.password
        obb.u_id = obj.manager_id
        obb.save()
        return vwupdmngr(request)
    return render(request,'manager/mupdateprofile.html',context)

def delete(request,idd):
    obj=Manager.objects.get(manager_id=idd)
    obj.delete()
    return vwupdmngr(request)

def vwupdmngr(request):
    ss=request.session["u_id"]
    obj=Manager.objects.filter(manager_id=ss)
    context={
        'b':obj
    }
    return render(request,'manager/viewupatemanager.html',context)