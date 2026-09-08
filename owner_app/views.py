from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from  admin_app .models import *

# Create your views here.




def owner_home(request):

    return render(request,'owner_home.html')



def owner_manage_branch(request):
    x=branch.objects.filter(owner_id=request.session['owner_id'])

    if request.method=='POST':
        branch_name=request.POST['branch_name']
        location=request.POST['location']
        phone=request.POST['phone']
        manager_name=request.POST['manager_name']

        add=branch(branch_name=branch_name,location=location,phone=phone,manager_name=manager_name,owner_id=request.session['owner_id'])
        add.save()

        return HttpResponse("<script>alert('Branch Added Successfully');window.location='/owner_manage_branch';</script>")

    return render(request,'owner_manage_branch.html',{'x':x})


def owner_update_branch(request,id):
    data=branch.objects.get(branch_id=id)

    if request.method=='POST':
        brach_name=request.POST['branch_name']
        location=request.POST['location']
        phone=request.POST['phone']
        manager_name=request.POST['manager_name']

        data.branch_name=brach_name
        data.location=location
        data.phone=phone
        data.manager_name=manager_name
        data.save()
        return HttpResponse("<script>alert('Branch Updated Successfuly');window.location='/owner_manage_branch';</script>")

    return render(request,'owner_manage_branch.html',{'data':data})


def owner_delete_branch(request,id):
    x=branch.objects.get(branch_id=id)
    x.delete()
    return HttpResponse("<script>alert('Delete Successfully');window.location='/owner_manage_branch';</script>")


def owner_manage_staff(request):
    br=branch.objects.filter(owner_id=request.session['owner_id'])
    data=staff.objects.filter(branch__owner_id=request.session['owner_id'])

    if request.method=='POST':
        branch_id=request.POST['branch_id']
        staff_name=request.POST['staff_name']
        gender=request.POST['gender']
        age=request.POST['age']
        phone=request.POST['phone']
        email=request.POST['email']
        address=request.POST['address']
        joining_date=request.POST['joining_date']
        photo=request.FILES['photo']
        username=request.POST['uname']
        password=request.POST['password']


        fs= FileSystemStorage()
        image=fs.save(photo.name,photo)

        log=login(user_name=username,password=password,user_type='staff')
        log.save()

        add=staff(branch_id=branch_id,name=staff_name,gender=gender,age=age,phone=phone,email=email,address=address,joining_date=joining_date,photo=image,login_id=log.pk)
        add.save()

        return HttpResponse("<script>alert('Staff Added Successfully');window.location='/owner_manage_staff';</script>")

    return render(request,'owner_manage_staff.html',{'br':br,'data':data})



def owner_delete_staff(request,id):
    x=staff.objects.get(staff_id=id)
    x.delete()
    return HttpResponse("<script>alert('Delete Successfully');window.location='/owner_manage_staff';</script>")



def owner_update_staff(request,id):
        
    return  render(request,'owner_manage_staff.html')
