from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
from operator import mod



class Location(models.Model): 
    location_id=models.IntegerField(primary_key=True)
    regional_group=models.CharField(max_length=100)
    
    def __str__(self):
        return self.regional_group

class Department(models.Model):
    department_id=models.IntegerField()
    name=models.CharField(max_length=100)
    location_id=models.ForeignKey(Location,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name

class Job(models.Model):
    job_id=models.IntegerField()
    function=models.CharField(max_length=100)

    
    def __str__(self):
        return self.function

class Employee(models.Model):
    emp_id=models.IntegerField()
    l_name=models.CharField(max_length=100)
    f_name=models.CharField(max_length=100)
    m_name=models.CharField(max_length=10)
    job_id=models.ForeignKey(Job,on_delete=models.CASCADE)
    mgr_id=models.IntegerField()
    hiredate=models.DateField()
    salary=models.IntegerField()
    comm=models.PositiveIntegerField(blank=True)
    department_id=models.ForeignKey(Department,on_delete=models.CASCADE)

   
    def __str__(self):
        return self.l_name, self.f_name, self.m_name

    

