from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.ItemListView.as_view(), name='index'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='details'),
    path('add/', views.ItemCreateView.as_view(), name='create_item'),
    path('edit/<int:pk>/', views.ItemUpdateView.as_view(), name='update_item'),
    path('delete/<int:pk>/', views.DeleteItemView.as_view(), name='delete_item'),
]