from .models import Order, Customer, Prodacts
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class former (ModelForm):
    class Meta:
        model =Order
        fields= '__all__'


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class updat(ModelForm):
    class Meta:
        model = Customer
        # fields = ['name', 'phone', 'email', 'img']
        fields = '__all__'
        exclude = ('user',)

class CreateProd(ModelForm):
    class Meta:
        model =Prodacts
        fields= '__all__'