from django.shortcuts import render
from .models import Order
# Create your views here.

#홈페이지
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

#주문하는 페이지
def order(request):
    

    return render(request, 'order.html',{'orders' : orders})


