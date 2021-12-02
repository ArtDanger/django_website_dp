from django.shortcuts import render
from .models import Order
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable
from .forms import OrderForm
from telebot.sendmessage import sendTelegram


# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.filter(type_price='gold').get()
    pc_2 = PriceCard.objects.filter(type_price='silver').get()
    pc_3 = PriceCard.objects.filter(type_price='bronze').get()
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form,
                }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:  # check for request
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', {'name': name, })
    else:  # displays a blank page
        return render(request, './thanks.html')
