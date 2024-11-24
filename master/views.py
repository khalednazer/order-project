from django.contrib.auth import authenticate, login, logout
from django.http import response
from django.shortcuts import redirect, render
from .models import Customer, Prodacts, Order, DataRecord
from .form import former, createUserForm, updat,CreateProd
from django.forms import inlineformset_factory
from .filter import FilterOrder
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decrators import authuser, allow
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login')
@allow(allows=['customer', 'admin'])
def account(request):
    edit = updat(instance=request.user.customer)

    dataFromModel = Customer.objects.get(user=request.user)
    print(dataFromModel)
    conOrder = dataFromModel.relation.all()
    allorderr = conOrder.count()
    pend = conOrder.filter(status = 'pending').count()
    done = conOrder.filter(status = 'deliveerd').count()


    if request.method =='POST':
        updated = updat(request.POST,request.FILES, instance=request.user.customer)
        if updated.is_valid:
            updated.save()
    return render(request, 'editeAccount.html', {'up':edit,
                                            'cus':dataFromModel,
                                            'total':allorderr,
                                            'delivered':done,
                                            'pend':pend,
                                            })


@login_required(login_url='login')
@allow(allows=['customer', 'admin'])
def user (request):
    cutt = Customer.objects.get(user=request.user)    
    allorder = cutt.relation.all()
    conOrder = cutt.relation.all().count()
    pend = allorder.filter(status = 'pending').count()
    done = allorder.filter(status = 'deliveerd').count()
    

    return render(request, 'user.html', {'name':request.user, 'allorder':allorder , 'total':conOrder, 'pend':pend, 'delivered':done})

@authuser
def register(request):
    newForm=createUserForm()
    if request.method =='POST':
        newForm= createUserForm(request.POST)
        if newForm.is_valid():
            user =newForm.save()
            # Customer.objects.create(user = user, name = user)

            name = newForm.cleaned_data.get('username')
            # userr=Group.objects.get(name='customer')
            # user.groups.add(userr)
            messages.success(request, "account was created " + name )
            return redirect('/Login')
    return render(request, 'register.html', {'new':newForm})


@authuser
def Login(request):
    if request.method == 'POST':
        nameuser = request.POST.get('username')
        paswords = request.POST.get('password')
        auth = authenticate(request, username = nameuser, password = paswords)
        if auth is not None:
            login(request, auth)
            custt = Customer.objects.get(name=nameuser)
            return redirect('cust/'+str(custt.id)) # name of the path from urls.py
        else :
            messages.warning(request, 'username or password incorrect')
            print('not founded')


    return render(request, 'login.html', {})

def logoutt(request):
    logout(request)
    return redirect('login')

def main (request):
    return render(request, 'main.html')

@login_required(login_url='login')
@allow(allows=['admin', 'customer'])
def cust (request, pk):
    print(pk)
    dataFromModel = Customer.objects.get(id=pk)
    allorder=dataFromModel.relation.all() #or you can use order_set
    totalorder = allorder.count()
    delverd=allorder.filter(status = 'deliveerd').count()
    pend=allorder.filter(status = 'pending').count()
    fliters = FilterOrder(request.GET, queryset=allorder)
    allorder=fliters.qs

    return render(request, 'customer.html', {'cus':dataFromModel,
                                            'total':totalorder,
                                            'custorder':allorder,
                                            'filter':fliters,
                                            'delivered':delverd,
                                            'pend':pend,

                                        })

@login_required(login_url='login')
def prod (request):
    dataFromModel = Prodacts.objects.all()
    cont = Prodacts.objects.all().count()
    return render(request, 'prodact.html', {'products':dataFromModel,'total':cont })

@login_required(login_url='login')
@allow(allows=['admin'])
def dahs (request):
    orders = Customer.objects.all()
    totals= Order.objects.all().count()
    allorder= Order.objects.all().order_by('-status')
    Delivered= Order.objects.filter(status='deliveerd').count()
    Pending= Order.objects.filter(status='pending').count()
    total = Customer.objects.all().count()

    return render(request, 'dash.html', {'ord':orders,
                                        'total':totals,
                                        'delivered':Delivered,
                                        'pend':Pending,
                                        'counCustomer':total,
                                        'forShow':allorder,
                                        
                                        })
@login_required(login_url='Login')
@allow(allows=['admin'])
def add_order (request):
    neworder= CreateProd()
    if request.method == 'POST':
        data_from_html=CreateProd(request.POST)
        if data_from_html.is_valid():
            data_from_html.save()
            return redirect('/')

    coi={
        'new':neworder
    }
    return render(request, 'add_order.html' , coi)


@login_required(login_url='login')
@allow(allows=['admin'])
def update_order(request, pk):
    order = Order.objects.get(id = pk)
    oldDate= former(instance= order)
    if request.method == 'POST':
        data = former(request.POST, instance=order)
        if data.is_valid():
            data.save()
            return redirect('/')
    return render(request, 'update.html',{'oldd':  oldDate})


@login_required(login_url='login')
@allow(allows=['admin'])
def delete(request, pk):
    ord = Order.objects.get(id=pk)
    if request.method == 'POST':
        if 'Yes' in request.POST:
            ord.delete()
            return redirect('/')

        if 'No' in request.POST:
            return redirect('/')
    return render(request, 'delete.html', {'orr':ord})


@login_required(login_url='Login')
@allow(allows=['admin','customer'])
def addMore(request, pk):
    cc = Customer.objects.get(id = pk)
    formset = inlineformset_factory(Customer, Order, fields=('prod', 'status'), extra=5) 
    shwofromset=formset(queryset=Order.objects.none(),  instance=cc)
    test= former(initial={'customer':cc})
    if request.method == 'POST':
        shwofromset=formset(request.POST, instance=cc)
        if shwofromset.is_valid():
                shwofromset.save()
                return redirect('/cust/'+str(pk))
        


    contain = {
        'form':former(initial={'customer':cc}),
        'cuu':shwofromset,
        'name':cc,
        'oldform':test,
    }
    return render(request, 'addmore.html', contain)



from .utils import import_excel  # ضع وظيفة الاستيراد في ملف utils.py

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['excel_file']
        # حفظ الملف مؤقتًا
        file_path = uploaded_file.name
        with open(file_path, 'wb') as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)
        
        # استيراد البيانات
        import_excel(file_path)
        return HttpResponse('Data imported successfully!')
    return render(request, 'upload.html')


def show(request):
    exl = DataRecord.objects.all()
    return render(request, 'show.html', {'data':exl})