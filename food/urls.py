from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='details'),
    path('add/', views.create_item, name='create_item'),
    path('edit/<int:item_id>/', views.update_item, name='update_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]