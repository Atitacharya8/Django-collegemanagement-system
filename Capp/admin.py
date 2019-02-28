from django.contrib import admin
# Register your models here.
from Capp.models import College, Department, Student, Library, Gallery, Account, Admission

admin.site.register([College,Department,Student,Library,Gallery,Account,Admission])