from django.http import HttpResponse
from django.shortcuts import render

from  admin_app .models import *

# Create your views here.




def owner_home(request):

    return render(request,'owner_home.html')



def owner_manage_branch(request):
    data=branch.objects.filter(owner_id=request.session['owner_id'])

    if request.method=='POST':
        branch_name=request.POST['branch_name']
        location=request.POST['location']
        phone=request.POST['phone']
        manager_name=request.POST['manager_name']

        add=branch(branch_name=branch_name,location=location,phone=phone,manager_name=manager_name,owner_id=request.session['owner_id'])
        add.save()

        return HttpResponse("<script>alert('Branch Added Successfully');window.location='/owner_manage_branch';</script>")

    return render(request,'owner_manage_branch.html',{'data':data})


def owner_update_branch(request,id):
    return render(request,'owner_manage_branch.html')

def owner_delete_branch(request,id):
    x=branch.objects.get(branch_id=id)
    x.delete()
    return HttpResponse("<script>alert('Delete Successfully');window.location='/owner_manage_branch';</script>")


def manage_staff(request):

    return render(request,'owner_manage_staff.html')


