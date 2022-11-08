from . import views
from django.urls import path

urlpatterns = [
    path('', views.toHome, name="Home"),   
    path('services', views.services, name="services"),   
    path('contact_us', views.contact_us, name="contact_us"),   
    path('order', views.Order, name="Order"),   
]
