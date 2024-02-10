from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError as MVDKE
from django.contrib.auth.models import User
from base.models import *
from shop.models import *
from blog.models import *

# Create your views here.

def about(request):
    settings = Settings.objects.latest('id')
    about = About.objects.latest('id')
    contact = Contact.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    gallery = Galery.objects.all()

    return render(request, 'about.html', locals())

def index(request):
    settings = Settings.objects.latest('id')
    products = ShopProduct.objects.all()[0:10]
    dishes = ShopDish.objects.all()[0:5]
    blogs = Blog.objects.all()[0:6]
    last_blog = Blog.objects.latest('id')
    gallery = Galery.objects.all()
    contact = Contact.objects.latest('id')

    return render(request, 'index.html', locals())

def error(request):
    error = Error.objects.latest('id')

    return render(request, '404.html', locals())

def faq(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    faq = Faq.objects.latest('id')
    contact = Contact.objects.latest('id')

    message = ''
    show_message = False
    if request.method == 'POST':
        show_message = True
        try:
            name = request.POST['name']
            if len(name) > 255:
                raise
            email = request.POST['email']
            if len(email) > 255:
                raise
            quest = request.POST['quest']
            if len(quest) > 255:
                raise
            message = request.POST['message']
            if len(email) > 50:
                raise

            HelpMessage.objects.create(name=name, email=email, quest=quest, message=message)
            message = 'Обращение успешно созданo!'
        except Exception:
            message = 'Ошибка: Не удалось создать обращение.'

    return render(request, 'faq.html', locals())

def reservation(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')

    message = ''
    if request.method == 'POST':
        show_message = True
        try:
            name = request.POST['name']
            if len(name) > 255:
                raise
            email = request.POST['email']
            if len(email) > 50:
                raise
            person = request.POST['person']
            phone = request.POST['phone']
            if len(phone) > 40:
                raise
            date = request.POST['date']
            time = request.POST['time']
            message = request.POST['message']

            Reservation.objects.create(name=name, email=email, person=person,\
                                     phone=phone, date=date, time=time, message=message)
            message = 'Бронирование успешно создано!'
        except:
            message = 'Ошибка при создании бронирования'
            
    return render(request, 'reservation.html', locals())

def login(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')

    show_message = False
    if request.method == 'POST':
        show_message = True
        login = request.POST['username']
        password = request.POST['password']
        try:
            checkbox = request.POST['checkbox']
            User.objects.get(username=login, password=password)
            message = 'Успешный вход!'
        except MVDKE:
            message = 'Политика конфиденциальности не принята'
        except User.DoesNotExist:
            message = 'Неверный логин или пароль'

    return render(request, 'login.html', locals())

def index_2(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')
    settings2 = SettingsTwo.objects.latest('id')
    gallery = Galery.objects.all()
    products = ShopProduct.objects.all()
    dishes = ShopDish.objects.all()
    blogs = Blog.objects.all()

    return render(request, 'index-2.html', locals())

def index_3(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')
    settings2 = SettingsTwo.objects.latest('id')
    settings3 = SettingsThree.objects.latest('id')
    gallery = Galery.objects.all()
    products = ShopProduct.objects.all()[0:12]
    dishes = ShopDish.objects.all()
    blogs = Blog.objects.all()

    return render(request, 'index-3.html', locals())

def index_4(request):
    settings = Settings.objects.latest('id')
    settings4 = SettingsFour.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')
    gallery = Galery.objects.all()
    products = ShopProduct.objects.all()
    dishes = ShopDish.objects.all()
    blogs = Blog.objects.all()
    categoryes = ShopCategory.objects.all()

    return render(request, 'index-4.html', locals())

def index_5(request):
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')
    settings = Settings.objects.latest('id')
    settings3 = SettingsThree.objects.latest('id')
    settings5 = SettingsFive.objects.latest('id')
    gallery = Galery.objects.all()
    categoryes = ShopCategory.objects.all()[0:12]
    products = ShopProduct.objects.all()
    dishes = ShopDish.objects.all()
    blogs = Blog.objects.all()

    return render(request, 'index-5.html', locals())

def contact(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')
    gallery = Galery.objects.all()

    message = ''
    show_message = False
    if request.method == 'POST':
        show_message = True
        try:
            terms = request.POST['terms']
            name = request.POST['name']
            if len(name) > 255:
                raise
            email = request.POST['email']
            if len(email) > 255:
                raise
            quest = request.POST['quest']
            if len(quest) > 255:
                raise
            message = request.POST['message']
            if len(email) > 50:
                raise

            HelpMessage.objects.create(name=name, email=email, quest=quest, message=message)
            message = 'Обращение успешно созданo!'
        except MVDKE:
            message = 'Ошибка: Политика конфиденциальности не принята.'
        except Exception:
            message = 'Ошибка: Не удалось создать обращение.'

    return render(request, 'contact.html', locals())

def coming_soon(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    coming = Coming.objects.latest('id')
    contact = Contact.objects.latest('id')

    return render(request, 'coming-soon.html', locals())

def signup(request):
    if request.method == 'POST':
        show_message = True
        try:
            name = request.POST['name']
            if len(name) > 255:
                raise
            checkbox = request.POST['checkbox']
            email = request.POST['email']
            if len(email) > 50:
                raise
            password = request.POST['password']
            if len(password) < 8:
                raise NameError
            password2 = request.POST['password_conf']
            if password != password2:
                raise TypeError
            User.objects.create(username=name, email=email, password=password)
            message = 'Пользователь успешно создан!'
        except NameError:
            message = 'Пароль должен содержать не менее 8 символов'
        except TypeError:
            message = 'Пароли не совпадают'
        except MVDKE:
            message = 'Политика конфиденциальности не принята'
        except:
            message = 'Ошибка при создании аккаунта'

    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')

    return render(request, 'signup.html', locals())

def terms(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')
    terms = Terms.objects.latest('id')

    return render(request, 'terms-conditions.html', locals())

def wishlist(request):
    settings = Settings.objects.latest('id')
    last_blog = Blog.objects.latest('id')
    contact = Contact.objects.latest('id')

    return render(request, 'wishlist.html', locals())