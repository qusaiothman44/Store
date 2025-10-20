from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    desc= models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category =models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')        
    name = models.CharField(max_length=255)
    desc= models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image = CloudinaryField('image', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_active=models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    created_at= models.DateTimeField(auto_now_add=True)
    is_paid= models.BooleanField(default=False)
    total_price= models.DecimalField(max_digits=10,decimal_places=2, default=0)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"



class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price= models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
