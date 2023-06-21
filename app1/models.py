from django.db import models

# Create your models here.
class Course(models.Model):
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=100)
    def __str__(self):
        return self.c_name
    
class Student(models.Model):
    c_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    s_name=models.CharField(max_length=100,primary_key=True)
    s_paid=models.IntegerField()
    def __str__(self):
        return self.s_name