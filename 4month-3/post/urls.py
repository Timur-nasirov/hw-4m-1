from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index'),
	path('contact/', contact, name='contact'),
	path('about/', about, name='about'),
	path('time/', time, name='time'),
	path('portfolio/', portfolio, name='portfolio')
]