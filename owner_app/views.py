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
    stt=staff.objects.get(staff_id=id)
    br=branch.objects.filter(owner_id=request.session['owner_id'])
    print(stt,"/////////")


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
        

        stt.branch_id=branch_id
        stt.staff_name=staff_name
        stt.gender=gender
        stt.age=age
        stt.phone=phone
        stt.email=email
        stt.address=address
        stt.joining_date=joining_date
        stt.photo=image
        stt.username=username
        stt.password=password
        stt.save()


        return HttpResponse("<script>alert('Updated Successfully');window.location='/owner_manage_staff';</script>")


    return  render(request,'owner_manage_staff.html',{'stt':stt,'br':br})




def owner_manage_product(request):
    stt=product_category.objects.all()
    br=branch.objects.filter(owner_id=request.session['owner_id'])
    pd=product.objects.filter(owner_id=request.session['owner_id'])

    if request.method=='POST':
        product_name=request.POST['product_name']
        brand=request.POST['brand']
        price=request.POST['price']
        stock=request.POST['stock']
        stock=request.POST['stock']
        description=request.POST['description']
        photo=request.FILES['image']
        expriry_date=request.POST['expriry_date']
        branch_id=request.POST['branch_id']
        category_id=request.POST['category_id']

        fs= FileSystemStorage()
        image=fs.save(photo.name,photo)

        add=product(product_name=product_name,brand=brand,price=price,stock=stock,description=description,image=image,expiry_date=expriry_date,branch_id=branch_id,category_id=category_id,owner_id=request.session['owner_id'])
        add.save()

        return HttpResponse("<script>alert('Add Successfully');window.location='/owner_manage_product';</script>")


    return render(request,'owner_manage_product.html',{'stt':stt,'br':br,'pd':pd})



def owner_delete_product(request,id):
    dele=product.objects.get(product_id=id)
    dele.delete()
    return HttpResponse("<script>alert('Delete Successfully');window.location='/owner_manage_product';</script>")


def owner_update_product(request,id):
    stt=product_category.objects.all()
    br=branch.objects.filter(owner_id=request.session['owner_id'])
    pd_data=product.objects.filter(owner_id=request.session['owner_id'])

    if request.method=='POST':
        product_name=request.POST['product_name']
        brand=request.POST['brand']
        price=request.POST['price']
        stock=request.POST['stock']
        stock=request.POST['stock']
        description=request.POST['description']
        photo=request.FILES['image']
        expriry_date=request.POST['expriry_date']
        branch_id=request.POST['branch_id']
        category_id=request.POST['category_id']


        fs= FileSystemStorage()
        image=fs.save(photo.name,photo)

        pd_data.product_name=product_name
        pd_data.brand=brand
        pd_data.price=price
        pd_data.stock=stock
        pd_data.description=description
        pd_data.image=image
        pd_data.expriy_date=expriry_date
        pd_data.branch_id=branch_id
        pd_data.category_id=category_id
        pd_data.save()

        return HttpResponse("<script>alert('Add Successfully');window.location='/owner_manage_product';</script>")

        
        
    
    return render(request,'owner_manage_product.html',{'stt':stt,'br':br,'pd_data':pd_data})

