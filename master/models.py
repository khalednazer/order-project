from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    img =models.ImageField(null=True, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.user)
    


class Prodacts(models.Model):
    choice=(
        ('indoor', 'indoor'),
        ('outdoor', 'outdoor'),
    )
    name = models.CharField(max_length=30)
    price= models.IntegerField()
    catgory=models.CharField(choices=choice, max_length=20 )
    descrip= models.CharField(max_length=100)
    data_created=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    stat=(
        ('pending', 'pending'),
        ('out for delivery', 'out for delivery'),
        ('deliveerd', 'deliveerd'),
    )
    customer =models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='relation')
    prod=models.ForeignKey(Prodacts, on_delete=models.SET_NULL, null=True)
    data_created=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status =models.CharField(choices=stat, max_length=30, default='pending')
    note = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self) -> str:
        return str(self.prod)
    
class profile(models.Model):
    user= models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
    firstName = models.CharField(max_length=30, null=True)
    secondName = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=15, null=True)

    def __str__(self) -> str:
        return str(self.user)
    



class DataRecord(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    def __str__(self) -> str:
        return self.name
    # أي حقول أخرى تتوافق مع بيانات Excel
