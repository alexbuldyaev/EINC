from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm

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

@login_required
def paypal_pay(request):
    paypal_dict = {
        "business": "acccko-facilitator@gmail.com",
        "amount": "100.00",
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


