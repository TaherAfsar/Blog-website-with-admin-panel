from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.


def home(req):
    blogs = Blog.objects.order_by("-date")
    return render(req,'home.html',{'blogs':blogs})
    #return HttpResponse("Hello World on about page") 
def about(req):
     return render(req,'about.html',{'data':[1,2,3,4,5]})
def details(req,id):
     blog = get_object_or_404(Blog,pk=id)
     return render(req,'detail.html',{'blog':blog})
