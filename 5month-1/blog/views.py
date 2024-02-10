from django.shortcuts import render
from blog.models import *
from base.models import *

# Create your views here.
def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    settings = Settings.objects.latest('id')
    gallery = Galery.objects.all()
    last_blog = Blog.objects.latest('id')
    create_comment = False

    if request.method == 'POST':
        author = request.POST['name']
        content = request.POST['message']
        Comment.objects.create(author=author, content=content, blog=blog)
        create_comment = True
    
    comments = Comment.objects.filter(blog=id)
    comment_count = len(comments)

    return render(request, 'blog-details.html', locals())

def blogs(request):
    blogs = Blog.objects.all()
    settings = Settings.objects.latest('id')
    gallery = Galery.objects.all()
    last_blog = Blog.objects.latest('id')

    return render(request, 'blogs.html', locals())