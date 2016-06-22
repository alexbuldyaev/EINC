from django.shortcuts import render, redirect
from django.utils import timezone
from .models import PolicyCar
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
import random

def post_list(request):
    return render(request, 'einc/results.html', {})

def post_count(request):
    return render(request, 'einc/count.html', {})
def post_countksk(request):
    return render(request, 'einc/countksk.html', {})
def post_counthom(request):
    return render(request, 'einc/counthome.html', {})
def post_signin(request):
    return render(request, 'einc/signin.html', {})
def post_bepay(request):
    return render(request, 'einc/bepay.html', {})
def post_contact(request):
    return render(request, 'einc/contact.html', {})
    
def mod_create(request, namecar,vin,regnum,docnum,doctype, summa, sk):   
    carr = {"1":"Ford","2":"Chevrolet","3":"LAda","4":"BMW","5":"Mercedes"}
    

    objec = PolicyCar(PolicyID=random.randint(3,100), PolicyType_id = 1, Status_id = 3, CarName = carr[(namecar)], CompName_id = sk, CarVIN = int(vin), CarRegNum=regnum, CarDocID=int(docnum), CarDocType=doctype, MonSum = int(summa), Driver_id = 1, Owner_id = 1, Insured_id = 1, User_id = 1)
    objec.save()
    return render(request, 'einc/count.html', {})

#def create_obj():
    
#sobstvdi = {"1":"fiz.face","2":"yur.face"}
 #   typedi = {"1":"Legkovoye","2":"Taaxi","3":"small lorry","4":"big lorry","5":"moto"}
  #  mestodi = {"1":"Moscow","2":"Moscow Sub","3":"Saint Petersberg","4":"SPB sub","5":"Altai"}
   # mosschdi = {"1":"50-","2":"50-70","3":"70-100","4":"100-120","5":"120-150","6":"150"}
    #minagedi = {"1":"22-","2":"22+"}
    #mineexpdi = {"1":"3-","2":"3+"}
    #discdi = {"1":3,"2":4,"3":5,"4":6,"5":7,"6":8,"7":9,"8":10}
    #discdi = {"1":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8}

def account_profile(request):
    return HttpResponse("Hi, {0}! Nice to meet you.".format(request.user.first_name))


def account_logout(request):
    logout(request)
    return redirect('/')


@csrf_exempt
def paypal_success(request):
    return HttpResponse("Money is mine. Thanks.")


def home(request):

    if request.user.is_authenticated():
        return HttpResponse("{0} <a href='/accounts/logout'>exit</a>".format(request.user))
    else:
        return HttpResponse("<a href='/login/vk-oauth2/'>login with VK</a>")

def add(request):
    return HttpResponse("Is added")


@login_required
def paypal_pay(request):
    paypal_dict = {
        "business": "alexbuldyaev-facilitator@gmail.com",
        "amount": PolicyCar.MonSum,
        "currency_code": "RUB",
        "item_name": "products in EINC",
        "invoice": "INV-00001",
        "notify_url": reverse('paypal-ipn'),
        "return_url": "http://alexbu.pythonanywhere.com/payment/success/",
        "cancel_return": "http://alexbu.pythonanywhere.com/payment/cart/",
        "custom": str(request.user.id)
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "paypal_dict": paypal_dict}
    return render(request, "einc/payment.html", context)


