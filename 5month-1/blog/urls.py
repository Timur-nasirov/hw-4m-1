from django.urls import path
from blog.views import *

urlpatterns = [
    path('<int:id>/', blog_details, name='blog-details'), 
    path('', blogs, name='blogs')
]