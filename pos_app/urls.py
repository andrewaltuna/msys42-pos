from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.openpos, name='openpos'),
    path('configure/', views.configure_item, name='configure-items'),

    #Config Item Actions
    path('add/', views.add_item, name='add-item'),
    path('update/<str:pk>/', views.update_item, name='update-item'),
    path('delete/<str:pk>/', views.delete_item, name='delete-item'),

    #Create Order
    path('order/confirm/', views.create_order, name='create-order'),
    path('nostock/', views.no_stock, name='no-stock')
]
