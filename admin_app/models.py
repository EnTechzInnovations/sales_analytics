from django.db import models

# Create your models here.


class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100)


class owner(models.Model):
    owner_id=models.AutoField(primary_key=True)
    login=models.ForeignKey('login',on_delete=models.CASCADE)
    shop_name=models.CharField(max_length=100)
    owner_name=models.CharField(max_length=100)
    photo=models.ImageField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    License=models.CharField(max_length=100)


class branch(models.Model):
    branch_id=models.AutoField(primary_key=True)
    owner=models.ForeignKey('owner',on_delete=models.CASCADE)
    branch_name=models.CharField(max_length=225)
    location=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    manager_name=models.CharField(max_length=225)




class staff(models.Model):
    staff_id=models.AutoField(primary_key=True)
    login=models.ForeignKey('login',on_delete=models.CASCADE)
    branch=models.ForeignKey('branch',on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    photo=models.ImageField(max_length=225)
    gender=models.CharField(max_length=225)
    age=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    address=models.CharField(max_length=225)
    joining_date=models.CharField(max_length=225)
    


class product_category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=225)
    description=models.CharField(max_length=225)


class product(models.Model):
    product_id=models.AutoField(primary_key=True)
    category=models.ForeignKey('product_category',on_delete=models.CASCADE)
    owner=models.ForeignKey('owner',on_delete=models.CASCADE)
    branch=models.ForeignKey('branch',on_delete=models.CASCADE)
    product_name=models.CharField(max_length=225)
    brand=models.CharField(max_length=225)
    price=models.CharField(max_length=225)
    stock=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    image=models.ImageField(max_length=225)
    expiry_date=models.CharField(max_length=225)


class customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    owner=models.ForeignKey('owner',on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=225)
    phone=models.ImageField(max_length=225)
    email=models.CharField(max_length=225)
    address=models.CharField(max_length=225)
    gender=models.CharField(max_length=225)

class sales(models.Model):
    sales_id=models.AutoField(primary_key=True)
    staff=models.ForeignKey('staff',on_delete=models.CASCADE)
    customer=models.ForeignKey('customer',on_delete=models.CASCADE)
    product=models.ForeignKey('product',on_delete=models.CASCADE)
    total_amount=models.CharField(max_length=225)
    payment_mode=models.CharField(max_length=225)
    bill_number=models.CharField(max_length=225)
    sales_date=models.CharField(max_length=225)


class sales_details(models.Model):
    sales_details_id=models.AutoField(primary_key=True)
    sales=models.ForeignKey('sales',on_delete=models.CASCADE)
    product=models.ForeignKey('product',on_delete=models.CASCADE)
    quantity=models.CharField(max_length=225)
    unit_price=models.CharField(max_length=225)
    sub_total_amount=models.CharField(max_length=225)


class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    login=models.ForeignKey('login',on_delete=models.CASCADE)
    complaint=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    reply=models.CharField(max_length=225)


class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    login=models.ForeignKey('login',on_delete=models.CASCADE)
    feedback=models.CharField(max_length=225)
    date=models.CharField(max_length=225)


