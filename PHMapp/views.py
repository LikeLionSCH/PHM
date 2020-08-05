from django.shortcuts import render
from .models import Order
# Create your views here.

def home(request) :
    orders = Order.objects.all()
    return render(request, 'home.html',{'orders' : orders})

#주문내역
def history(request):
    orders = Order.objects.all()
    return render(request, 'history.html',{'orders' : orders})

#주문내역 수정
def edit(request):
    pass

