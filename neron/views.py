from django.shortcuts import render
from random import sample
from apps.store.models import Product
from apps.diseño.models import Banner, HomeImage

# Declare sus funciones

def home(request):
    
    products = Product.objects.all().filter(is_available=True)
    banners = Banner.objects.all()
    homeCard = HomeImage.objects.all()

    # Muestra de productos al Azar - Inicio
    productAzar = sample(list(products), min(4, len(products)))
    # Muestra de productos al Azar - Fin
    
    context = {
        'products': products,
        'banners': banners,
        'homeCard': homeCard,
        'productAzar': productAzar,
    }
    
    return render(request, 'home.html', context)