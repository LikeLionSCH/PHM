from django.shortcuts import render, redirect, get_object_or_404
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
def order(request, bamin_id ):
    orders_imformation = get_object_or_404(Order,pk=bamin_id )
    if request.method == "POST" :
        if orders_imformation.is_vaid():
            orders_imformation.save()
            return redirect('home')

    return render(request, 'order.html',{'orders' : orders})


