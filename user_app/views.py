from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.template import response

from  admin_app .models import *

# Create your views here.


def updatepasslocation(request):
    data={}

    login_id=request.GET.get('logid')
    latitude=request.GET.get('latti')
    longitude=request.GET.get('latti')

    print(login_id,"_________________")

    try:
        qrylog=owner.objects.get(login_id=login_id)
        qrylog.latitude=latitude
        qrylog.longitude=longitude
        qrylog.save()
        
        status="success"


    except owner.DoesNotExist:
        status= "error"
        message="Invalid credentails"

    response = {

        'status': status,
        'data':data,
        'method':'updatepasslocation'
    }
  

    if status == "error":
        response['message'] = message
    print(status)
    
    return JsonResponse(response)



def user_register(request):

    data={}
    fname=request.GET.get('fname')
    phone=request.GET.get('phone')
    email=request.GET.get('email')
    place=request.GET.get('place')
    latitude=request.GET.get('latitude')
    longitude=request.GET.get('longitude')
    uname=request.GET.get('uname')
    paswd=request.GET.get('password')

    try:
        qrylog=login(user_name=uname,password=paswd,user_type="user")
        qrylog.save()
        qryuser=user(name=fname,email_id=email,place=place,phone=phone,login_id=qrylog.pk,latitude=latitude,longitude=longitude)
        qryuser.save()
        status="success"

    except login.DoesNotExist:
        status= "error"
        message="Invalid credentails"

    response = { 

        'status': status,
        'data':data
    }

    if status == "error":
        response['message'] = message
    print(status)
    return JsonResponse(response)
    


def user_login(request):
    data=[]
    username=request.GET.get('username')  
    passw=request.GET.get('password')
    

    try:
        queryset=login.objects.filter(user_name=username,password=passw)
        for q in queryset:
            data.append({
                
                'login_id' : q.login_id,
                'username' : q.user_name,
                'password' : q.password,
                'user_type': q.user_type

            })
        if data:
            status = "success"
        else:
            status = "error"
            message= "Invalid credential"

    except login.DoesNotExist:
        status= "error"
        message = "Invalid credential"

    response ={
        'status' : status,
        'data': data
    }
    print(data)

    if status == "error":
        response['message'] = message
    
    return JsonResponse(response)



def user_send_complaints(request):
    data={}
    date=date = datetime.now().date()
    comp=request.GET.get('complaints')
    login_id=request.GET.get('userid')


    try:
        qrylog=complaint(complaint=comp,date=date,login_id=login_id,reply="pending")
        qrylog.save()
        
        status="success"


    except complaint.DoesNotExist:
        status= "error"
        message="Invalid credentails"

    response = {

        'status': status,
        'data':data,
        'method':'send'
    }


    if status == "error":
        response['message'] = message
    print(status)
    
    return JsonResponse(response)



def User_view_complaints(request):
    data=[]
    login_id=request.GET.get('user_id')  
    

    try:
        queryset=complaint.objects.filter(login_id=login_id)
        for q in queryset:
            data.append({
                
                'complaint_id' : q.complaint_id,
                'complaints' : q.complaint,
                'date' : q.date,
                'reply': q.reply

            })
        if data:
            status = "success"
        else:
            status = "error"
            message= "No complaints found"

    except complaint.DoesNotExist:
        status= "error"
        message = "No complaints found"

    response ={
        'status' : status,
        'data': data,
        'method': 'view'
    }
    
    print(data)

    if status == "error":
        response['message'] = message
    
    return JsonResponse(response)




def user_send_feedback(request):
    data={}
    date=date = datetime.now().date()
    feed=request.GET.get('feedback')
    login_id=request.GET.get('userid')


    try:
        qrylog=feedback(feedback=feed,date=date,login_id=login_id)
        qrylog.save()
        
        status="success"


    except feedback.DoesNotExist:
        status= "error"
        message="Invalid credentails"

    response = {

        'status': status,
        'data':data
    }
    data['method']='send'

    if status == "error":
        response['message'] = message
    print(status)
    
    return JsonResponse(response)






def User_view_shops(request):
    data = []

    lati = request.GET.get('lati')
    logi = request.GET.get('logi')

    print(lati,"_________________")

    print(logi,"___________________")


    if not lati or not logi:
        return JsonResponse({
            'status': 'error',
            'message': 'Latitude and longitude are required',
            'method': 'view'
        })

    try:
        lati = float(lati)
        logi = float(logi)

        shops = owner.objects.all()

        for q in shops:
            try:
                shop_lat = float(q.latitude)
                shop_lon = float(q.longitude)

                # Distance calculation in miles
                import math

                lat1 = math.radians(lati)
                lon1 = math.radians(logi)
                lat2 = math.radians(shop_lat)
                lon2 = math.radians(shop_lon)

                dlat = lat2 - lat1
                dlon = lon2 - lon1

                a = (
                    math.sin(dlat / 2) ** 2 +
                    math.cos(lat1) *
                    math.cos(lat2) *
                    math.sin(dlon / 2) ** 2
                )

                distance = 3959 * 2 * math.asin(math.sqrt(a))

                # 11.068 miles
                if distance < 11.068:
                    data.append({
                        'owner_id': q.owner_id,
                        'shop_name': q.shop_name,
                        'owner_name': q.owner_name,
                        'photo': q.photo.url if q.photo else '',
                        'phone': q.phone,
                        'email': q.email,
                        'address': q.address,
                        'district': q.district,
                        'state': q.state,
                        'pincode': q.pincode,
                        'License': q.License,
                        'latitude': q.latitude,
                        'longitude': q.longitude,
                        'distance': round(distance, 2)
                    })

            except (ValueError, TypeError):
                # Skip shops with invalid latitude/longitude
                continue

        # Sort nearest shop first
        data.sort(key=lambda x: x['distance'])

        if data:
            status = "success"
        else:
            status = "error"
            message = "No shops found nearby"

    except (ValueError, TypeError):
        status = "error"
        message = "Invalid latitude or longitude"

    response = {
        'status': status,
        'data': data,
        'method': 'view'
    }

    if status == "error":
        response['message'] = message

    return JsonResponse(response)





def User_view_products(request):
    data = []

    owner_id = request.GET.get('owner_id')

    if not owner_id:
        return JsonResponse({
            'status': 'error',
            'message': 'Owner ID is required',
            'data': [],
            'method': 'view'
        })

    try:
        products = product.objects.filter(owner_id=owner_id)

        for q in products:
            data.append({
                'product_id': q.product_id,
                'product_name': q.product_name,
                'brand': q.brand,
                'description': q.description,
                'price': q.price,
                'stock': q.stock,
                'photo': q.image.url if q.image else '',
                'category_id': q.category_id,
                'owner_id': q.owner_id,
                'branch_id': q.branch_id,
                'expiry_date': q.expiry_date
            })

        if data:
            status = 'success'
            message = 'Products found'
        else:
            status = 'error'
            message = 'No products found for this owner'

    except (ValueError, TypeError):
        status = 'error'
        message = 'Invalid owner ID'

    return JsonResponse({
        'status': status,
        'data': data,
        'message': message,
        'method': 'view'
    })



from datetime import datetime

from django.db import transaction
from django.http import JsonResponse



def User_add_book_to_take_away(request):
    data = {}
    status = "error"
    message = ""

    product_id = request.GET.get('product_id')
    quantity = request.GET.get('quantity')
    login_id = request.GET.get('userid')
    payment = request.GET.get('payment', 'CASH')   # UPI / CASH / CARD

    try:
        # Validate input
        if not product_id or not quantity or not login_id:
            raise ValueError("Missing product, quantity or user")

        qty = int(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be at least 1")

        if payment not in ("UPI", "CASH", "CARD"):
            raise ValueError("Invalid payment method")

        with transaction.atomic():
            prod = product.objects.select_for_update().get(pk=product_id)
            usr = user.objects.get(login_id=login_id)   # see note 2

            # Check stock and reduce it
            current_stock = int(prod.stock)
            if qty > current_stock:
                raise ValueError(f"Only {current_stock} in stock")
            prod.stock = current_stock - qty
            prod.save()

            # Save the booking (don't name the variable "booking",
            # it would shadow the model class)
            new_booking = booking(
                product_id=prod,
                user_id=usr,
                date=str(datetime.now().date()),
                payment_mode=payment,
                quantity=str(qty),
                status="pending",
            )
            new_booking.save()

        status = "success"
        message = "Booking added successfully"

    except product.DoesNotExist:
        message = "Product not found"
    except user.DoesNotExist:
        message = "User not found"
    except Exception as e:
        message = f"Error occurred: {str(e)}"

    response = {
        'status': status,
        'data': data,
        'message': message,
        'method': 'add_to_cart',   # matches the Android response() check
    }

    return JsonResponse(response)