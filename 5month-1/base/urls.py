from django.urls import path
from base.views import *

urlpatterns = [
    path('about/', about, name='about'),
    path('', index, name='index'),
    path('index-2/', index_2, name='index-2'),
    path('index-3/', index_3, name='index-3'),
    path('index-4/', index_4, name='index-4'),
    path('index-5/', index_5, name='index-5'),
    path('faq/', faq, name='faq'),
    path('404/', error, name='404'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('coming/', coming_soon, name='coming-soon'),
    path('reservation/', reservation, name='reservation'),
    path('signup/', signup, name='signup'),
    path('terms/', terms, name='terms-conditions'),
    path('wishlist/', wishlist, name='wishlist')
]