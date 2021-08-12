from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def landing_page(request):
    return HttpResponse("Hello, World! Nama Saya Ariq")


def profile(request):
    return HttpResponse("profile ku")


def count(request, angka):
    angka = angka+1
    return HttpResponse(str(angka))


def sapa(request, nama):
    return HttpResponse("Halo "+nama)


def example(request):
    return render(request, 'example.html')


def newpage(request):
    return HttpResponse("new")


def a(request):
    return HttpResponse()


def coba(request):
    return render(request, 'coba.html')


def shop(request):
    return render(request, 'shop.html')



def shop_laptop(request):
    return render(request, 'shop_laptop.html')


def shop_console(request):
    return render(request, 'shop_console.html')


def shop_smartphone(request):
    return render(request, 'shop_smartphone.html')


def first_page(request):
    return render(request, 'firstpage.html')


def second_page(request):
    return render(request, 'secondpage.html')


def shop_laptop_list(request):
    try:
        print(request.GET)
        category_laptop = Category.objects.get(pk=1)
        #pk == primary_key
        if(request.GET=={}):
            product_laptop = Product.objects.filter(category=category_laptop)
        else:
            product_laptop= Product.objects.filter(category=category_laptop).filter(
                name__icontains=request.GET['product_name'])

        # WHERE name like 'chrome'
        if(product_laptop.count() != 0):
            return render(request, 'shop_laptop_list.html', {'product_list': product_laptop, 'available': True})
        else:
            return render(request, 'shop_laptop_list.html', {'available': False})
    except:
        return HttpResponse("Terjadi Error")


# Create your views here.
