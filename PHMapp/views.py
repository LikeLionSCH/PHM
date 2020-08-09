from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
# Create your views here.

#홈페이지
def home(request) :
    return render(request, 'home.html')

#주문내역
def history(request):
    orders = Order.objects.all()
    return render(request, 'history.html', {'orders': orders})

#주문내역 수정
def edit(request, bamin_id):
    order = get_object_or_404(Order, pk = bamin_id)
    
    if request.method=='POST':
        #사진 파일 있는지 확인
        if 'image' in request.FILES:
            order.image = request.FILES['image']
        order.price = request.POST['price']
        order.customer = request.POST['customer']
        order.address = request.POST['address']
        order.request = request.POST['request']
        order.food = request.POST['food']

        order.save()
        return redirect('history')
    return render(request, 'edit.html',{'order' : order})

#주문하는 페이지
def order(request):
    if request.method == 'POST':
        order = Order()
        #사진 파일 있는지 확인
        if 'image' in request.FILES:
            order.image = request.FILES['image']
        order.price = request.POST['price']
        order.customer = request.POST['customer']
        order.address = request.POST['address']
        order.request = request.POST['request']
        order.food = request.POST['food']

        order.save()
        return redirect('history')
    else:
        orders = Order.objects.all()
        return render(request, 'order.html', {'orders': orders})

# 준비 중 페이지
def ready(request):
    return render(request, 'ready.html')

# 주문 취소
def cancel(request, bamin_id):
    order = get_object_or_404(Order, pk=bamin_id)
    order.delete()
    return redirect('history')