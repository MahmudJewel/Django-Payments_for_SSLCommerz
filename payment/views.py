from django.shortcuts import render, redirect
from .forms import PaymentForm
# Create your views here.


def home(request):
    template_name = 'home.html'
    payment_form = PaymentForm()

    if request.method == "POST":
        payment_form = PaymentForm(request.POST, request.FILES)
        if payment_form.is_valid():
            print('The values are ==> ', payment_form)
            return redirect('/')

    context = {
        'payment_form': payment_form,
    }
    return render(request, template_name, context)
