from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
# Create your views here.
def insert_course(request):
    cn=input('enter the co_name:')
    id=int(input('enter your id :'))
    co=Course.objects.get_or_create(c_id=id,c_name=cn)[0]
    co.save()
    
    return HttpResponse('Course record is created')

def insert_student(request):
    cn=input('enter the co_name:')
    id=int(input('enter your id :'))
    Co=Course.objects.get_or_create(c_id=id,c_name=cn)[0]
    Co.save()

    sn=input("enter student name:")
    sp=int(input('enter the student payment:'))
    Su=Student.objects.get_or_create(c_id=Co,s_name=sn,s_paid=sp)[0]
    Su.save()

    return HttpResponse('Student record is created')


