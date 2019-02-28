from django.db import models

# Create your models here.
# class Home(models.Model):
class College(models.Model):
    name=models.CharField(max_length=250,default="Cosmos college of management and information technology")




class Department(models.Model):
    dept_name=models.CharField(max_length=250)


class Student(models.Model):
    name=models.CharField(max_length=250)

class Account(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)



class Library(models.Model):
    emp_name=models.CharField(max_length=250)



class Admission(models.Model):
    name=models.CharField(max_length=250)



class Gallery(models.Model):
    images=models.ImageField(upload_to="Capp")


