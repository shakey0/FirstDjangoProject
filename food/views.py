from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm


def get_actual_price(price):
    price = '£' + str(price / 100)
    if str(price)[-2] == '.':
        return price + '0'
    return price


def index(request):
    all_items_ordered = Item.objects.order_by('item_name')
    all_items = list(all_items_ordered)
    for item in all_items:
        item.actual_price_display = get_actual_price(item.item_price)
    context = {
        'all_items': all_items
    }
    return render(request, 'index.html', context)


def details(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return HttpResponse('No item found')
    item.item_price = get_actual_price(item.item_price)
    context = {
        'item': item
    }
    return render(request, 'details.html', context)


def create_item(request):
    if request.method == 'POST':
        
        post_data = request.POST.copy()
        item_price = post_data.get('item_price', '')
        if item_price.startswith('£'):
            post_data['item_price'] = item_price.replace('£', '').strip()
            post_data['item_price'] = int(round(float(post_data['item_price']) * 100))
        
        form = ItemForm(post_data)
        if form.is_valid():
            item = form.save(commit=False)  # Create an item instance but don't save it to the database yet
            if not item.item_image:  # Check if the item_image field is empty
                item.item_image = 'https://convida.pt/images/POIs/Restaurantes_01.jpg'  # Set the default URL
            item.save()  # Save the item to the database
            return redirect('food:index')
    else:
        form = ItemForm(initial={'item_image': ''})
    
    return render(request, 'item-form.html', {'form': form})


def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        
        post_data = request.POST.copy()
        item_price = post_data.get('item_price', '')
        if item_price.startswith('£'):
            post_data['item_price'] = item_price.replace('£', '').strip()
            post_data['item_price'] = int(round(float(post_data['item_price']) * 100))
        
        form = ItemForm(post_data, instance=item)
        if form.is_valid():
            form.save()
            return redirect(reverse('food:details', kwargs={'item_id': item_id}))
    else:
        item.item_price = get_actual_price(item.item_price)
        form = ItemForm(instance=item)
    
    return render(request, 'item-form.html', {'form': form, 'item': item})


def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'delete-item.html', {'item': item})
