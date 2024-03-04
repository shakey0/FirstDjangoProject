from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1, blank=True)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, blank=True, default='https://convida.pt/images/POIs/Restaurantes_01.jpg')
    
    def get_absolute_url(self):
        return reverse('food:details', kwargs={'pk': self.pk})