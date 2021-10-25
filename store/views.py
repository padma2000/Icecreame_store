from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from datetime import datetime
from store.models import Contact_info
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from .models import Product, Contact_info

# Create your views here.
def index(request):
    products=Product.objects.all()
    print(products)
    n = len(products)
    params={'product': products,'nCard':n }
    if request.user.is_anonymous:
        return redirect("/loginpage")
    return render(request, 'index.html',params)

def about(request):
    contact_info = Contact_info.objects.all()
    params={'contact':contact_info}
    return render(request, 'about.html', params)


def Services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        contact = Contact_info(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent!')
    return render(request, 'contact.html')

def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('/')
            return response
        else:
            return render(request, 'loginpage.html')
    return render(request, 'loginpage.html')

def logout_view(request):
    logout(request)
    return redirect('/loginpage')

def tracker(request):
    console.log('tracker')

