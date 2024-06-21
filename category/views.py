from django.shortcuts import render
from category.models import Category

# Create your views here.


def categry(request):
    obk=""
    if request.method=='POST':
        obj=Category()
        obj.category=request.POST.get('ctgy')
        obj.save()
        obk ="success"
    context = {
            'msg':obk
        }
    return render(request,'category/category.html',context)
