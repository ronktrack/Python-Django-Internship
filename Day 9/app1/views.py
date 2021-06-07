from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def myform(request):
    return render(request,'myform.html')

def process(request):
    print("welcome")
    print(request.method)
    print(request.POST)
    a = int(request.post['n1'])
    b = int(request.post['n2'])
    c = a + b
    return render(request,'ans.html',{'sum':c,'n1':a,'n2':b})