from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *


# Create your views here.
def openpos(request):
    all_items = item.objects.all()
    return render(request, 'pos_app/openpos.html', {'item' : all_items})

def configure_item(request):
    all_items = item.objects.all()
    return render(request, 'pos_app/configure.html', {'item' : all_items})

def add_item(request):
    form = itemForm()
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configure')
    context = {'form':form}
    return render(request, "pos_app/form_add.html", context)

def update_item(request, pk):
    pitem = item.objects.get(id=pk)
    form = itemForm(instance=pitem)
    if request.method == 'POST':
        form = itemForm(request.POST, instance=pitem)
        if form.is_valid():
            form.save()
            return redirect('/configure')
    context = {'form':form}
    return render(request, "pos_app/form_add.html", context) 

def delete_item(request, pk):
    pitem = item.objects.get(id=pk)
    pitem.delete()
    return redirect('/configure')

def create_order(request):
    if request.method == 'POST':
        check = 1

        items = request.POST.get('complete_order')
        pmethod = request.POST.get('payment_method')
        totamt = request.POST.get('total_amount')

        items_omit = items[:-1]
        item_list = items_omit.split("-")
        for i in item_list:
            item_inst = item.objects.get(pk=i[0])
            iprice = item_inst.item_price
            line_total = iprice * int(i[2])
            if (item_inst.stock_quantity - int(i[2])) < 0:
                return redirect("/nostock")
            else:
                if check == 1:
                    corder = order.objects.create(order_total=totamt, order_method=pmethod)
                    check = 0
                item_order.objects.create(item_id = item_inst, order_id = corder, line_total=line_total, item_order_qty=i[2])
                item_inst.stock_quantity = item_inst.stock_quantity - int(i[2])
                item_inst.save()
    return redirect('/')

def no_stock(request):
    return render(request, "pos_app/nostock.html")