from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item
from .forms import ItemForm


def get_actual_price(price):
    price = '£' + str(price / 100)
    if str(price)[-2] == '.':
        return price + '0'
    return price


class ItemListView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'all_items'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('item_name')
        for item in queryset:
            item.actual_price_display = get_actual_price(item.item_price)
        return queryset


class ItemDetailView(DetailView):
    model = Item
    template_name = 'details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'].item_price = get_actual_price(context['item'].item_price)
        return context


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item-form.html'
    success_url = reverse_lazy('food:index')
    
    def get_initial(self):
        return {'item_image': ''}
    
    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        item_price = post_data.get('item_price', '')
        if item_price.startswith('£'):
            item_price = item_price.replace('£', '').strip()
            post_data['item_price'] = int(round(float(item_price) * 100))
        
        request.POST = post_data
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if not form.instance.item_image:
            form.instance.item_image = 'https://convida.pt/images/POIs/Restaurantes_01.jpg'
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item-form.html'
    
    def get_success_url(self):
        return reverse('food:details', kwargs={'pk': self.object.pk})

    def get_initial(self):
        return {'item_price': get_actual_price(self.object.item_price)}
    
    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        item_price = post_data.get('item_price', '')
        if item_price.startswith('£'):
            item_price = item_price.replace('£', '').strip()
            post_data['item_price'] = int(round(float(item_price) * 100))
        
        request.POST = post_data
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if not form.instance.item_image:
            form.instance.item_image = 'https://convida.pt/images/POIs/Restaurantes_01.jpg'
        return super().form_valid(form)


class DeleteItemView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'delete-item.html'
    success_url = reverse_lazy('food:index')
