from django.shortcuts import render
from feedback.models import Feedback
from user.models import User
from turf.models import Turf

# Create your views here.

def avwfb(request):
    obj=Feedback.objects.all()
    context={
        'a':obj
    }
    return render(request,'feedback/aviewfeedback.html',context)


def fb(request):
    ss=request.session["u_id"]
    obk=""
    obb=Turf.objects.all()
    if request.method=='POST':
        obj=Feedback()
        obj.user_id=ss
        obj.feedback=request.POST.get('fb')
        obj.turf_id=request.POST.get('nmt')
        obj.save()
        obk="ok"
    context = {
        't': obb,
        'msg':obk
    }
    return render(request,'feedback/feedback.html',context)

def mvwfb(request):
    ss=request.session["u_id"]
    obj=Feedback.objects.filter(turf__manager_id=ss)
    context={
        'b':obj
    }
    return render(request,'feedback/mviewfeedback.html',context)


