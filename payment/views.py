from django.shortcuts import render, redirect
from .forms import PaymentForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
STORE_ID = settings.STORE_ID
STORE_KEY = settings.STORE_KEY

@csrf_exempt
def home(request):
    print(f"STORE_ID = {settings.STORE_ID}")
    template_name = 'home.html'
    payment_form = PaymentForm()
    # print('======================')
    # print(mypayment)
    # print('======================')
    if request.method == "POST":
        # payment_form = PaymentForm(request.POST, request.FILES)
        # if payment_form.is_valid():
        #     print('The values are ==> ', payment_form)
        #     return redirect('/')
        mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=STORE_ID, sslc_store_pass=STORE_KEY)
        mypayment.set_urls(success_url='http://127.0.0.1:8000/success', fail_url='http://127.0.0.1:8000/fail', cancel_url='http://127.0.0.1:8000/cancel') # ipn_url='example.com/payment_notification'
        mypayment.set_product_integration(total_amount=Decimal('20.20'), currency='BDT', product_category='clothing', product_name='demo-product', num_of_item=2, shipping_method='YES', product_profile='None')
        mypayment.set_customer_info(name='John Doe', email='johndoe@email.com', address1='demo address', address2='demo address 2', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111111')
        mypayment.set_shipping_info(shipping_to='demo customer', address='demo address', city='Dhaka', postcode='1209', country='Bangladesh')
        response_data = mypayment.init_payment()
        print('========= >>>>>>>  ', response_data)
        # return redirect('/')
        return redirect('https://sandbox.sslcommerz.com/EasyCheckOut/testcdecb531862bddf05aa7b070994f5efaef5')

    context = {
        'payment_form': payment_form,
    }
    return render(request, template_name, context)
