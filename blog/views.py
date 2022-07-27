from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.


def home(req):
    blogs = Blog.objects.all()
    return render(req,'home.html',{'blogs':blogs})
    #return HttpResponse("Hello World on about page") 
def about(req):
     return render(req,'about.html',{'data':[1,2,3,4,5]})
