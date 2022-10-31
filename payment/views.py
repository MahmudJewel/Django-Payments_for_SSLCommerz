from django.shortcuts import render, redirect
from .forms import PaymentForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.

from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
STORE_ID = settings.STORE_ID
STORE_KEY = settings.STORE_KEY


@csrf_exempt
def home(request):
    template_name = 'home.html'
    payment_form = PaymentForm()
    if request.method == "POST":
        payment_form = PaymentForm(request.POST, request.FILES)
        amount = 0
        if payment_form.is_valid():
            amount=payment_form.cleaned_data['amount']
            # print('=========>> ', type(amount))
        # print('=========>> ', payment_form.get['amount'])
        status_url = request.build_absolute_uri(reverse('status'))
        success_url = request.build_absolute_uri(reverse('success'))
        fail_url = request.build_absolute_uri(reverse('fail'))
        cancel_url = request.build_absolute_uri(reverse('cancel'))
        mypayment = SSLCSession(
            sslc_is_sandbox=True, sslc_store_id=STORE_ID, sslc_store_pass=STORE_KEY)
        mypayment.set_urls(success_url=success_url, fail_url=fail_url,
                           cancel_url=cancel_url, ipn_url=status_url)  # ipn_url= notification
        mypayment.set_product_integration(total_amount=Decimal(amount), currency='BDT', product_category='clothing',
                                          product_name='demo-product', num_of_item=2, shipping_method='YES', product_profile='None')
        mypayment.set_customer_info(name='John Doe', email='johndoe@email.com', address1='demo address',
                                    address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01713447790')
        mypayment.set_shipping_info(shipping_to='demo customer', address='demo address',
                                    city='Dhaka', postcode='1209', country='Bangladesh')
        response_data = mypayment.init_payment()
        # print('========= >>>>>>>  ', response_data)
        return redirect(response_data['GatewayPageURL'])

    context = {
        'payment_form': payment_form,
    }
    return render(request, template_name, context)


# ssl status for payment
@csrf_exempt
def ssl_status(request):
    template_name = 'status.html'
    if request.method == 'POST' or request.method == 'post':
        payment_data = request.POST
        print('status ===========> ', payment_data)
        status = payment_data['status']
        if status == 'VALID':
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            return HttpResponseRedirect(reverse('ssl_complete', kwargs={'val_id': val_id, 'tran_id': tran_id}))
    return render(request, template_name)


@csrf_exempt
def ssl_complete(reequest, val_id, tran_id):
    print('Completed ===========> ')
    return redirect('/')


# successful payment url
@csrf_exempt
def success(request):
    print('Success ===========> ')
    template_name = 'success.html'
    return render(request, template_name)

# failed payment url
@csrf_exempt
def fail(request):
    template_name = 'fail.html'
    print('Failed ===========> ')
    return render(request, template_name)

# canceled payment url
@csrf_exempt
def cancel(request):
    template_name = 'cancel.html'
    print('Canceled ===========> ')
    return render(request, template_name)

# # successful payment url
# @csrf_exempt
# def success(request):
#     template_name = 'success.html'
#     return render(request, template_name)
