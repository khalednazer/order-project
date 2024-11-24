from django.contrib import admin
from .models import Customer, Prodacts, Order,profile,DataRecord
# Register your models here.

admin.site.register(Customer)
admin.site.register(Prodacts)
admin.site.register(Order)
# admin.site.register(profile)
admin.site.register(DataRecord)