
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import Product, Order




class home(TemplateView):
    template_name = 'home.html'


def ecommerce_page(request):
    context = {
        'title': 'Ecommerce Page',
        'products': [
            {'name': 'Product 1', 'price': 10.99},
            {'name': 'Product 2', 'price': 19.99},
            {'name': 'Product 3', 'price': 29.99},
        ]
    }
    return render(request, 'home.html', context)



#def home(request):
 #   products = Product.objects.all()
  #  return render(request, 'home.html', {'products': products})


#def order(request):
 #   if request.method == 'POST':
  #      customer_name = request.POST['customer_name']


#def pagamento(request, forma_pagamento=None):
 #   if request.method == 'POST':
  #      forma_pagamento == request.POST['forma_pagamento']


