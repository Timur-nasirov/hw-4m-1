from django.shortcuts import render
from datetime import datetime as dt

# Create your views here.
def index(request):
	context = {
        'title': "Главная страница",
        'description': "Geeks",
        'greetings': "Добро пожаловть!",
        'benefits': ["это Geeks", "Удобный коворкинг", "Отличные преподователи", "Бесплатные ноутбуки"]
    }
	return render(request, 'post/index.html', context)

def about(request):
	context = {
        'title': "О нас",
        'description': "О нас",
        'greetings': "Добро пожаловть!",
        'numbers': ['200+ студентов', '70+ менторов', '50+ выпускников', '5+ филиалов']
    }
	return render(request, 'post/about.html', context)

def contact(request):
	context = {
        'title': "Контакты",
        'description': "Свяжитесь с нами",
        'phone': "0771244745",
        'instagram': "https://www.instagram.com/_abdykadyrov_s/",
        'telegram': "https://t.me/Abdykadyrov_S"
    }
	return render(request, 'post/contact.html', context)

def time(request):
	context = {
		'title': 'Время',
		'description': 'Узнать время',
		'time': dt.now().strftime('%H:%M:%S')
	}
	return render(request, 'post/time.html', context)

def portfolio(request):
	context = {
		'title': 'Наши проекты',
		'description': 'Наши проекты',
		'projects': ['NTphone2.2', 'Neotelecom_US', 'DopMath', 'SchoolNews']
	}
	return render(request, 'post/portfolio.html', context)