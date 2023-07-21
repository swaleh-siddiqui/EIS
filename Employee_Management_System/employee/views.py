from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):

    eror = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['employeeid']
        em = request.POST['emailid']
        pwd = request.POST['createpassword']

        try:
            user = User.objects.create_user(first_name = fn,last_name = ln, username = ec, password = pwd, email=em)
            EmployeeSignup.objects.create(user = user , empcode = ec)
            eror = "yes"
        except:
            eror = "no"

    return render(request,"register.html",locals())

def emp_login(request):
    eror = ""
    if request.method == "POST":
        u = request.POST['employeeid']
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        if user:
            login(request,user)
            eror = "yes"
        else :
            eror = "no"
    return render(request,"emp_login.html",locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    return render(request,"emp_home.html")

def profile(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")
    return render(request,"profile.html")

def Logout(request):
    logout(request)
    return redirect("index")

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect("emp_login")

    eror = ""
    user = request.user
    employee = EmployeeSignup.objects.get(user = user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['emailid']
        dob = request.POST['dateofbirth']
        bg = request.POST['bloodgroup']
        g = request.POST['gender']
        adhar = request.POST['aadharno']
        pan = request.POST['panno']
        b_acc = request.POST['bankaccountno']
        ifsc = request.POST['ifsccode']
        fname = request.POST['fathername']
        mname = request.POST['mothername']
        mstat = request.POST['maritalstatus']
        cont = request.POST['contactno']
        ad = request.POST['address']
        dep = request.POST['department']
        des = request.POST['designation']

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.user.email = em

        if dob:
            employee.dob = dob   

        employee.adhar = adhar
        employee.bank_acc = b_acc
        employee.pan = pan
        employee.ifsc_code = ifsc
        employee.address = ad
        employee.status = mstat
        employee.blood_grp =  bg
        employee.contact = cont
        employee.empdept = dep
        employee.designation = des
        employee.gender = g
        employee.father_name = fname
        employee.mother_name = mname


        try:
            employee.save()
            employee.user.save()
            eror = "yes"
        except:
            eror = "no"

    return render(request,"edit_profile.html",locals())

