from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key = True)
    phone = models.TextField(null = True)
    role = models.TextField(null = True)
    salary = models.FloatField(null = True)
    gender = models.TextField(null = True)
    dateOfBirth = models.TextField(null = True)
    ussername = models.TextField(null = True)
    password = models.TextField(null = True)
    fullname = models.TextField(null = True)
    lastname = models.TextField(null = True)
    firstname = models.TextField(null = True)
    address = models.TextField(null = True)
    
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE,default = 0)
    title = models.TextField(null = True)
    summary = models.TextField(null = True)
    numOfPage = models.IntegerField(null = True)
    author = models.TextField(null = True)
    image_path = models.TextField(null = True)
    publisher = models.TextField(null = True)
    categorical = models.TextField(null = True)
    language = models.TextField(null= True)

class BookItem(models.Model):
    id = models.AutoField(primary_key=True)
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE,default = 0)
    bookID = models.ForeignKey(Book,on_delete=models.CASCADE,default = 0)
    barcode = models.TextField(null = True)
    price = models.FloatField(null = True)
    discount = models.FloatField(null = True)

    

    
class ElectronicItem(models.Model):
    id = models.AutoField(primary_key=True)
    
class Laptop(models.Model) :
    id = models.AutoField(primary_key=True)


    