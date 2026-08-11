from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.



def home(request):

    return render(request,'home.html')


def login_section(request):

    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pass']

        try:
            lg=login.objects.get(user_name=username,password=password)

            if  lg.user_type=='admin':
                return HttpResponse("<script>alert('login success');window.location='/admin_home';</script>")
            
        except:
            return HttpResponse("<script>alert('Invalid Username or Password');window.location='/login';</script>")
              

    return render(request,'login.html')



def owner_register(request):

    if request.method=='POST':
        shop_name=request.POST['shop_name']
        owner_name=request.POST['owner_name']
        photo=request.FILES['photo']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        district=request.POST['district']
        state=request.POST['state']
        pincode=request.POST['pincode']
        license=request.FILES['license']
        username=request.POST['user_name']
        password=request.POST['password']

        fs= FileSystemStorage()
        image1=fs.save(photo.name,photo)

        
        fs= FileSystemStorage()
        image2=fs.save(license.name,license)

        lg=login(user_name=username,password=password,user_type='pending')
        lg.save()

        own=owner(shop_name=shop_name,owner_name=owner_name,photo=image1,phone=phone,email=email,address=address,district=district,state=state,pincode=pincode,License=image2,login=lg)
        own.save()


        return HttpResponse("<script>alert('Registration Sucess');winow.location='/login';</script>")



    return render(request,'owner_registration.html')




   

def admin_home(request):

    return render(request,'admin_home.html')



def admin_view_onwer(request):
    data=owner.objects.all()
    return render(request,'admin_view_owner.html',{'data':data})




