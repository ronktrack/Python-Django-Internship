from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return render(request,"home.html",{})

def aboutpageview(request):
    return render(request,"about.html")

def contactpageview(request):
    return render(request,"contact.html")

def formpageview(request):
    return render(request,"form.html")

def process(request):
    print("welcome")
    print(request.method)
    print(request.POST)
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    phone = request.POST['phone']
    age = int(request.POST['age'])
    dob = request.POST['dob']
    gender = request.POST['gender']
    city = request.POST['city']
    skill = request.POST['skill']
    return render(
        request,"ans.html",{
            'myname':name,
            'myemail':email,
            'mypassword':password,
            'myphone':phone,
            'myage':age,
            'mydob':dob,
            'mygender':gender,
            'mycity':city,
            'myskill':skill,
         } )