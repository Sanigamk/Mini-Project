from django.db.models import Q
from django.shortcuts import render
from user.models import User
from login.models import Login

# Create your views here.

def prfledit(request,idd):
    obb=User.objects.get(user_id=idd)
    context={
        'a':obb
    }
    if request.method=="POST":
        obj=User.objects.get(user_id=idd)
        obj.name=request.POST.get('unm')
        obj.age=request.POST.get('uge')
        obj.house_name=request.POST.get('uhn')
        obj.post=request.POST.get('upost')
        obj.pin=request.POST.get('upin')
        obj.district=request.POST.get('udst')
        obj.email=request.POST.get('umail')
        obj.password=request.POST.get('upsw')
        obj.phn_no=request.POST.get('upn')
        obj.save()

        obb = Login.objects.get(u_id=request.session['u_id'],type='user')
        obb.email = obj.email
        obb.password = obj.password
        obb.u_id = obj.user_id
        obb.save()
        return uvwupdtpf(request)
    return render(request,'user/profileedit.html',context)

def delete(request,idd):
    obj=User.objects.get(user_id=idd)
    obj.delete()
    return uvwupdtpf(request)



def user(request):
    obk =""
    if request.method=="POST":
        a = request.POST.get('umail')
        b = request.POST.get('upn')
        obv = User.objects.filter(Q(email=a) & (Q(phn_no=b) | Q(email=a) | Q(phn_no=b)))
        if len(obv) > 0:
            obk = "User exist"
        else:
            obj=User()
            obj.name=request.POST.get('unm')
            obj.age=request.POST.get('uage')
            obj.house_name=request.POST.get('uhs')
            obj.post=request.POST.get('upst')
            obj.pin=request.POST.get('upin')
            obj.district=request.POST.get('ust')
            obj.email=request.POST.get('umail')
            obj.phn_no=request.POST.get('upn')
            obj.password=request.POST.get('upsw')
            obj.save()

            obb = Login()
            obb.email=obj.email
            obb.password=obj.password
            obb.type="user"
            obb.u_id=obj.user_id
            obb.save()
            obk = "success"
    context = {
            'msg': obk
        }
    return render(request,'user/user.html',context)


def uvwupdtpf(request):
    ss = request.session["u_id"]
    obj=User.objects.filter(user_id=ss)
    context={
        'a':obj
    }
    return render(request,'user/uviewupdateprofile.html',context)