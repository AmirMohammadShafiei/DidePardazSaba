from django.shortcuts import render,redirect
from .models import Phone, Brand
from .forms import MobileForm
from .models import Phone

def mobile_list(request):
    mobiles = Phone.objects.all()
    return render(request, 'inventory/mobile_list.html', {'mobiles': mobiles})

def mobile_create(request):
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobile_list')
    else:
        form = MobileForm()
    return render(request, 'inventory/mobile_form.html', {'form': form})

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'inventory/brand_list.html', {'brands': brands})


def mobile_list2(request):
    nationality = request.GET.get('nationality', None)
    if nationality:
        brands = Brand.objects.filter(nationality=nationality)
        mobiles = Phone.objects.filter(brand__in=brands)
    else:
        mobiles = Phone.objects.all()

    nationalities = Brand.objects.values_list('nationality', flat=True).distinct()
    
    return render(request, 'inventory/mobile_list.html', {
        'mobiles': mobiles,
        'nationalities': nationalities,
    })


from django.shortcuts import render
from .models import Phone, Brand

def mobile_search(request):
    nationality = request.GET.get('nationality', None)
    if nationality:
        brands = Brand.objects.filter(nationality=nationality)
        mobiles = Phone.objects.filter(brand__in=brands)
    else:
        mobiles = Phone.objects.all()
    
    brand_name = request.GET.get('brand_name', '').strip()
    if brand_name:
        try:
            brand = Brand.objects.get(name=brand_name)
            mobiles = mobiles.filter(brand=brand)
        except Brand.DoesNotExist:
            mobiles = Phone.objects.none()
    
    nationalities = Brand.objects.values_list('nationality', flat=True).distinct()
    
    return render(request, 'inventory/mobile_list.html', {
        'mobiles': mobiles,
        'nationalities': nationalities,
        'brand_name': brand_name,
    })


def phones_with_matching_nationality(request):
    phones = Phone.objects.all()
    
    brand_nationalities = {brand.id: brand.nationality for brand in Brand.objects.all()}
    
    matching_phones = [
        phone for phone in phones
        if brand_nationalities.get(phone.brand_id) == phone.manufacturing_country
    ]
    
    return render(request, 'inventory/filter.html', {'phones': matching_phones})



