from django.urls import path
from . import views

urlpatterns = [
    path('clientCreds/', views.ClientCredentialView.as_view(), name= 'clientCredentials'),
    path('shipments/', views.ShipmentView.as_view(), name= 'shipments'),
    path('orders/', views.OrderView.as_view(), name= 'orders'),
]