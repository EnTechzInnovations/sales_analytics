from django.http import HttpResponse
from django.shortcuts import render
from  admin_app .models import *
from datetime import datetime

# Create your views here.




def staff_home(request):
    return render(request,'staff_home.html')



def staff_view_profile(request):
    data=staff.objects.get(login_id=request.session['login_id'])
    return render(request,'staff_view_profile.html',{'data':data})



def staff_send_complaint(request):
    date=date = datetime.now().date()
    comp=complaint.objects.filter(login_id=request.session['login_id'])
    if request.method=='POST':
        complaints=request.POST['complaint']

        x=complaint(complaint=complaints,login_id=request.session['login_id'],date=date,reply='pending')
        x.save()

        return HttpResponse("<script>alert('Complaint Send Successfully');window.location='/staff_send_complaint';</script>")

    return render(request,'staff_send_complaint.html',{'comp':comp})





# 1. Record Sales Transactions
def staff_record_sales(request):

    staff_data = staff.objects.get(
        login_id=request.session['login_id']
    )

    products = product.objects.filter(
        branch=staff_data.branch
    )

    if request.method == 'POST':

        # Customer Details
        customer_name = request.POST['customer_name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gender']

        # Product Details
        product_id = request.POST['product']
        quantity = int(request.POST['quantity'])
        payment_mode = request.POST['payment_mode']

        # Get Product
        prod = product.objects.get(
            product_id=product_id
        )

        # Check Stock
        if int(prod.stock) < quantity:

            return HttpResponse(
                "<script>alert('Insufficient Stock');"
                "window.location='/staff_record_sales';</script>"
            )

        # Add Customer
        cust = customer(
            branch=staff_data.branch,
            customer_name=customer_name,
            phone=phone,
            email=email,
            address=address,
            gender=gender
        )

        cust.save()

        # Generate Bill Number
        last_sale = sales.objects.order_by('-sales_id').first()

        if last_sale:

            bill_number = "BLNO" + str(
                100 + last_sale.sales_id + 1
            )

        else:

            bill_number = "BLNO101"

        # Calculate Total
        total_amount = int(prod.price) * quantity

        # Save Sales
        sale = sales(
            staff=staff_data,
            customer=cust,
            product=prod,
            total_amount=total_amount,
            payment_mode=payment_mode,
            bill_number=bill_number,
            sales_date=datetime.now().date()
        )

        sale.save()

        # Save Sales Details
        detail = sales_details(
            sales=sale,
            product=prod,
            quantity=quantity,
            unit_price=prod.price,
            sub_total_amount=total_amount
        )

        detail.save()

        # Reduce Stock
        prod.stock = int(prod.stock) - quantity
        prod.save()

        return HttpResponse(
            "<script>alert('Sale Recorded Successfully. Bill No: "
            + bill_number +
            "');window.location='/staff_record_sales';</script>"
        )

    return render(
        request,
        'staff_record_sales.html',
        {
            'products': products
        }
    )

# 2. View Product List
def staff_view_products(request):

    staff_data = staff.objects.get(login_id=request.session['login_id'])

    products = product.objects.filter(
        branch=staff_data.branch
    )

    return render(
        request,
        'staff_view_products.html',
        {'products': products}
    )


# 3. Search Products
def staff_search_products(request):

    staff_data = staff.objects.get(login_id=request.session['login_id'])

    products = product.objects.filter(
        branch=staff_data.branch
    )

    if request.method == 'POST':

        product_name = request.POST['product_name']

        products = product.objects.filter(
            branch=staff_data.branch,
            product_name__icontains=product_name
        )

    return render(
        request,
        'staff_search_products.html',
        {'products': products}
    )


def staff_manage_customers(request):

    staff_data = staff.objects.get(
        login_id=request.session['login_id']
    )

    customers = customer.objects.filter(
        branch=staff_data.branch
    )

    return render(
        request,
        'staff_manage_customers.html',
        {
            'customers': customers
        }
    )

# 5. View Customer Details
def staff_view_customer_details(request, id):

    data = customer.objects.get(
        customer_id=id
    )

    return render(
        request,
        'staff_view_customer_details.html',
        {'data': data}
    )


from datetime import datetime, timedelta
from decimal import Decimal


def staff_view_daily_sales(request):

    staff_data = staff.objects.get(
        login_id=request.session['login_id']
    )

    today = datetime.now().date()

    # Today's Sales
    today_data = sales.objects.filter(
        staff=staff_data,
        sales_date=today
    )

    # Weekly Sales (Monday to Sunday)
    week_start = today - timedelta(days=today.weekday())

    weekly_data = sales.objects.filter(
        staff=staff_data,
        sales_date__gte=week_start,
        sales_date__lte=today
    )

    # Monthly Sales
    month_start = today.replace(day=1)

    monthly_data = sales.objects.filter(
        staff=staff_data,
        sales_date__gte=month_start,
        sales_date__lte=today
    )

    # Yearly Sales
    year_start = today.replace(month=1, day=1)

    yearly_data = sales.objects.filter(
        staff=staff_data,
        sales_date__gte=year_start,
        sales_date__lte=today
    )

    # All Sales
    total_data = sales.objects.filter(
        staff=staff_data
    )

    # Calculate total amount
    def calculate_total(data):
        return sum(
            (Decimal(str(i.total_amount)) for i in data),
            Decimal('0')
        )

    # Select sales period
    period = request.GET.get('period', 'daily')

    if period == 'daily':
        data = today_data
    elif period == 'weekly':
        data = weekly_data
    elif period == 'monthly':
        data = monthly_data
    elif period == 'yearly':
        data = yearly_data
    else:
        data = total_data

    data = data.order_by('-sales_id')

    context = {
        'today': today,

        'today_total': calculate_total(today_data),
        'weekly_total': calculate_total(weekly_data),
        'monthly_total': calculate_total(monthly_data),
        'yearly_total': calculate_total(yearly_data),
        'total_sales': calculate_total(total_data),

        'today_count': today_data.count(),
        'weekly_count': weekly_data.count(),
        'monthly_count': monthly_data.count(),
        'yearly_count': yearly_data.count(),
        'total_count': total_data.count(),

        'data': data,
        'period': period,
    }

    return render(
        request,
        'staff_view_daily_sales.html',
        context
    )

# 7. View Takeaway Product Bookings
def staff_view_takeaway_bookings(request):

    staff_data = staff.objects.get(
        login_id=request.session['login_id']
    )

    data = booking.objects.filter(
        product_id__branch=staff_data.branch
    ).order_by('-booking_id')

    for i in data:
        i.total_amount = (
            float(i.product_id.price) * int(i.quantity)
        )

    return render(
        request,
        'staff_view_takeaway_bookings.html',
        {'data': data}
    )

# 8. Update Booking Status to Paid
def staff_update_booking_status(request, id):

    staff_data = staff.objects.get(
        login_id=request.session['login_id']
    )

    data = booking.objects.get(
        booking_id=id,
        product_id__branch=staff_data.branch
    )

    data.status = 'paid'
    data.save()

    return HttpResponse(
        "<script>alert('Booking Status Updated to Paid');"
        "window.location='/staff_view_takeaway_bookings';</script>"
    )




def staff_customer_purchase_history(request, id):

    staff_data = staff.objects.get(
        login_id=request.session['login_id']
    )

    cust = customer.objects.get(
        customer_id=id,
        branch=staff_data.branch
    )

    purchase_history = sales.objects.filter(
        customer=cust
    ).order_by('-sales_id')

    return render(
        request,
        'staff_customer_purchase_history.html',
        {
            'customer': cust,
            'purchase_history': purchase_history
        }
    )