from tabnanny import check
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.template import loader
from django.core.files.storage import FileSystemStorage
import itertools
from django.views.generic import ListView, DetailView, View
from .models import Book,BookItem,Employee
from django.contrib.auth.hashers import check_password


def index(request):
    print(request)
    # temp = loader.get_template('company.html')
    all_book = Book.objects.values()
    all_item_book = BookItem.objects.values()
    # list_book = all_book.union(all_item_book)
    all_laptop = None
    print(list_book)
    if all_book :
        str_res = ""
        list_book = []
        for b in all_book:
            # print(b.author)
            list_book.append(b)

        return render(request,"test_app/company.html", {"tmp_register":"",
                                                    "tmp_login":"",
                                                    "register_status":"Logout",
                                                    "login_status":request.session["member_name"],
                                                    'books':all_book})
    print("id: ",request.session.get("member_id"))
    if request.session.get("member_id"):
            return render(request,"test_app/company.html", {"tmp_register":"",
                                                    "tmp_login":"",
                                                    "register_status":"Logout",
                                                    "login_status":request.session["member_name"]})
    return render(request,"test_app/company.html", {"tmp_register":"register",
                                                    "tmp_login":"login",
                                                    "register_status":"Register",
                                                    "login_status":"Login"})
    
def bookshop_view(request):
    print(request)
    # temp = loader.get_template('company.html')
    all_book = BookItem.objects.values()
    print(all_book)
    if all_book :
        str_res = ""
        list_book = []
        for b in all_book:
            # print(b.author)
            list_book.append(b)

        return render(request,"test_app/company.html", {'books':all_book})
    print(request.session.test_cookie_worked())
    if request.session.get("member_id"):
            return render(request,"test_app/company.html", {"tmp_register":"",
                                                    "tmp_login":"",
                                                    "register_status":"Logout",
                                                    "login_status":request.session["member_name"]})
    return render(request,"test_app/company.html", {"tmp_register":"register",
                                                    "tmp_login":"login",
                                                    "register_status":"Register",
                                                    "login_status":"Login"})


def add_item_view(request):
    print("request:",request)
    # temp = loader.get_template('company.html')
    if request.method == "POST":
        id_employee = request.session["member_id"]
        employee = Employee.objects.get(id = id_employee)
        print("request.Post:", request.POST)
        data_form = request.POST
        print(request.FILES)
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        print(file_url)
        print(file)
        book = Book()
        book.title = data_form.get('title')
        book.author = data_form.get("author")
        book.image_path = file_url
        book.employeeID = employee
        book.categorical = data_form.get("categorical")
        book.publisher = data_form.get("publisher")
        book.summary = data_form.get("summary")
        book.language = data_form.get("language")
        book.numOfPage = int(data_form.get("nop"))
        book.save()
        bookitem = BookItem()
        bookitem.bookID = book
        bookitem.employeeID = employee
        bookitem.barcode = data_form.get("barcode")
        bookitem.price = float(data_form.get("price"))
        bookitem.save()
        return redirect("/testapp/hoaileba")
    else:
        return render(request,"test_app/addcompany.html")
   
   
def register_view(request):
    if request.method == "POST":
        data_form = request.POST
        employee = Employee()
        employee.phone = data_form.get("phone")
        employee.role = data_form.get("role")
        employee.salary = 1000
        employee.gender = data_form.get("gender")
        employee.dateOfBirth = data_form.get("dob")
        employee.fullname = data_form.get("fullname")
        employee.firstname = data_form.get("firstname")
        employee.lastname = data_form.get("lastname")
        employee.address = data_form.get("address")
        employee.password = data_form.get("password")
        employee.ussername = data_form.get("username")
        employee.save()

        return redirect("/testapp/login")
    
    else:
        return render(request,"test_app/register.html")

def login_view(request):
    if request.method == "POST":
        data_form = request.POST
        m = Employee.objects.get(ussername=request.POST['username'])
        password = m.password
        print(password, data_form.get("password"))
        print(check_password(data_form.get("password"),password))
        if password == data_form.get("password"): 
            request.session['member_id'] = m.id   
            request.session['member_name'] = m.fullname  
            return redirect("/testapp/hoaileba",)
        else:
            return render(request,"test_app/login.html")
    else:
        return render(request,"test_app/login.html")