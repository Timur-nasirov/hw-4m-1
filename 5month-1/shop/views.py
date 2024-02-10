from django.shortcuts import render
from shop.models import *
from blog.models import *
from base.models import *

# Create your views here.
def shop_details(request, id):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')
    product = ShopProduct.objects.get(id=id)
    
    if request.method == 'POST':
        show_message = True
        try:
            name = request.POST['name']
            if len(name) > 255:
                raise
            content = request.POST['content']
            ProductComment.objects.create(name=name, content=content, product=product)
            message = 'Комментарий спешно создан'
        except:
            message = 'Ошибка при создании коментария'

    comments = ProductComment.objects.filter(product=product)
    return render(request, 'shop-details.html', locals())

def shop(request):
    last_blog = Blog.objects.latest('id')
    settings = Settings.objects.latest('id')
    gallery = Galery.objects.all()
    contact = Contact.objects.latest('id')
    products = ShopProduct.objects.all()

    return render(request, 'shop.html', locals())

def cart(request):
    settings = Settings.objects.latest('id')
    gallery = Galery.objects.all()
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')

    return render(request, 'cart.html', locals())

def checkout(request):
    message = ''
    show_message = False
    if request.method == 'POST':
        show_message = True
        try:
            name = request.POST['name']
            if len(name) > 255:
                raise
            surname = request.POST['surname']
            if len(surname) > 255:
                raise
            phone = request.POST['phone']
            if len(phone) > 30:
                raise
            email = request.POST['email']
            if len(email) > 50:
                raise
            city = request.POST['city']
            if len(name) > 50:
                raise
            country = request.POST['country']
            if len(country) > 2:
                raise
            domofon = request.POST['domofon']
            if len(domofon) > 30:
                raise
            Pay.objects.create(name=name, surname=surname, phone=phone, email=email, city=city, country=country, domofon=domofon)
            message = 'Заявка на оплату успешно создана!'
        except Exception:
            message = 'Ошибка при отправке заявки.'
    settings = Settings.objects.latest('id')
    gallery = Galery.objects.all()
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')

    return render(request, 'checkout.html', locals())

def category(request, name):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')
    category = ShopCategory.objects.get(title=name)
    products = ShopProduct.objects.filter(category=category)

    return render(request, 'category.html', locals())

def menu(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')
    menus = Menu.objects.all()

    return render(request, 'menu.html', locals())
