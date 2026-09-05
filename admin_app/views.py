from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, request
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
            request.session['login_id']=lg.pk

            if  lg.user_type=='admin':
                return HttpResponse("<script>alert('login success');window.location='/admin_home';</script>")

            if lg.user_type=='owner':
                ow=owner.objects.get(login_id=  request.session['login_id'])
                
                if ow:
                    request.session['owner_id']=ow.pk

                return HttpResponse("<script>alert('login success');window.location='/owner_home';</script>")
            
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



def admin_view_owner(request):
    data=owner.objects.all()
    return render(request,'admin_view_owner.html',{'data':data})


def  admin_accept_owner(request,id):
    x=login.objects.get(login_id=id)
    x.user_type='owner'
    x.save()
    return HttpResponse("<script>alert('Accept Successfully');window.location='/admin_home';</script>")
    


def admin_reject_owner(request,id):
    x=login.objects.get(login_id=id)
    x.user_type='reject'
    x.save()
    return HttpResponse("<script>alert('Reject Successfully');window.location='/admin_home';</script>")


def admin_view_staff(request):
    data=staff.objects.all()
    return render(request,'admin_view_staff.html',{'data':data})


def admin_manage_category(request):
    x=product_category.objects.all()
    if request.method=='POST':
        category_name=request.POST['cat_name']
        des=request.POST['desp']
        x=product_category(category_name=category_name,description=des)
        x.save()
        return HttpResponse("<script>alert('Add Successfully');window.location='/admin_home';</script>")

    return render(request,'admin_manage_category.html',{'x':x})



def admin_delete_category(request,id):
    x=product_category.objects.get(category_id=id)
    x.delete()
    return HttpResponse("<script>alert('Delete Successfully');window.location='/admin_home';</script>")



def admin_update_category(request,id):
    data=product_category.objects.get(category_id=id)

    if request.method=='POST':
        category_name=request.POST['cat_name']
        des=request.POST['desp']

        data.category_name=category_name
        data.description=des

        data.save()


        return HttpResponse("<script>alert('Update Successfully');window.location='/admin_home';</script>")
           
    return render(request,'admin_manage_category.html',{'data':data})




def  admin_view_feedback(request):
    data=feedback.objects.all()
    return render(request,'admin_view_feedback.html',{'data':data})


def admin_view_complaint(request):
    data=complaint.objects.all()

    return render(request,'admin_view_complaint.html',{'data':data})


def admin_send_reply(request,id):
    data=complaint.objects.get(complaint_id=id)

    if request.method=='POST':
        reply=request.POST['reply']
        data.reply=reply
        data.save()
        return HttpResponse("<script>alert('Reply Send Successfully');window.location='/admin_home';</script>")

    return render(request,'admin_send_reply.html')


