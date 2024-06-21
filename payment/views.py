from django.shortcuts import render
from payment.models import Payment
from turf.models import Turf
from booking.models import Booking
from user.models import User
from slots.models import Slots
import datetime

# Create your views here.


def mvwpay(request):
    ss=request.session["u_id"]
    obj=Payment.objects.filter(slot__turf__manager_id=ss)
    context={
        'a':obj
    }
    return render(request,'payment/mviewpayment.html',context)


def pay(request,idd):
    obo=""
    ss=request.session["u_id"]

    obb=Slots.objects.get(slot_id=idd)
    obk=User.objects.get(user_id=ss)
    context = {
        'v': obb,
    }

    if request.method=="POST":
        obj=Payment()
        obj.slot_id=idd
        obj.user_id=ss
        obj.card_holder_name=request.POST.get('pn')
        obj.date=datetime.datetime.now()
        obj.cvv=request.POST.get('cvv')
        obj.amount=request.POST.get('amnt')
        obj.status="Paid"
        obj.save()

        return HttpResponseRedirect('/payment/bill/' + str(obj.pay_id))
    return render(request,'payment/payment.html',context)


#Bill generate

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
#To Generate Checklist pdf
# def index(request,idd,pid):
from turf_management import settings

def index(request, idd):
    # return HttpResponse('hello')
    # print("helloooooooooo")
    print(idd)
    ob = Payment.objects.get(pay_id=idd)
    context = {
        'ok': ob,
    }

    template_path = 'payment/bill.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bill.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    fpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + str(ob.user_id) + ".pdf"

    # create a pdf
    outfile = open(fpath, "w+b")
    # pisa_status = pisa.CreatePDF(
    #     html, dest=response)
    pisa_status = pisa.CreatePDF(html, dest=outfile)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response
    return render(request, 'payment/bill.html', context)