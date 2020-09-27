from django.shortcuts import render,HttpResponse,redirect
from .forms import EmployeeForm
from .models import Employee,CompanyHead,TopEmployee
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def indexpage(request):
    data = CompanyHead.objects.all
    topemployee = TopEmployee.objects.all
    all_post = Paginator(Employee.objects.filter(),15)
    page = request.GET.get('page')
    try:
        posts = all_post.page(page)
    except PageNotAnInteger:
        posts = all_post.page(1)
    except:
        posts = all_post.page(all_post.num_pages)

    params = {
    'employee': posts ,
    'companyhead': data,
    'topemployee': topemployee
    }
    if request.user.is_authenticated:
        return render(request,'index.html',params)
    if not request.user.is_authenticated:
        return redirect('login')   

def signin(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('show-employee')
        else:
            messages.error(request,'Wrong Aministration')
            return render(request,'login.html')

def signout(request):
    auth.logout(request)
    messages.success(request,'Admin just logged out.')
    return redirect('login')


def login(request):
    return render(request,'login.html')

def load_form(request):
    form = EmployeeForm
    return render(request,'forms.html',{'form':form})

def add(request):
    form = EmployeeForm(request.POST)
    eid = request.POST['eid']
    if Employee.objects.filter(eid=eid).exists():
        messages.error(request, 'Ops Employee is already preset with same ID.')
        return redirect('loadform')
    else:
        form.save()
        messages.success(request,'Wow, 1 New Employee has been recorded.')
        return redirect('show-employee')


def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html',{'employee':employee})

    

def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    messages.success(request, 'Employee details is successfully updated')
    return redirect('show-employee')

def delete(request,id):
     employee = Employee.objects.get(id=id)
     employee.delete()
     messages.error(request,'Ops, Your 1 record is deleted.')
     return redirect('show-employee')   

def about(request):
     return render(request,'about.html') 

def show(request):
    all_post = Paginator(Employee.objects.filter(),15)
    page = request.GET.get('page')
    try:
        posts = all_post.page(page)
    except PageNotAnInteger:
        posts = all_post.page(1)
    except:
        posts = all_post.page(all_post.num_pages)

    params = {
    'employee': posts ,
    }
    return render(request,'show.html',params)          

def search(request):
    q = request.GET.get('q')
    posts = Employee.objects.filter(
        Q(ename__icontains = q)
        ).distinct()


    params = {
    'employee': posts,
    'query': f'{q}'
    }
    return render(request,'show.html',params)

