from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Orders

def toHome(request):   
    return render(request , 'Home.html')

def services(request):   
    return render(request , 'Services.html')

def contact_us(request):   
    return render(request , 'Contact_Us.html')

def Order(request):   
  if request.method == "POST":
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    service = request.POST['service']
    description = request.POST['description']
    address = request.POST['address']

    new_order = Orders(name = name, email = email, phone = phone , service = service, description = description, address = address)
    new_order.save()
    messages.success(request, "Order sent successfully.")
  return render(request , 'Order.html')