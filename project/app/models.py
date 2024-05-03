from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_email =models.EmailField()
    stu_city =models.CharField(max_length=100)
    stu_contact = models.IntegerField()