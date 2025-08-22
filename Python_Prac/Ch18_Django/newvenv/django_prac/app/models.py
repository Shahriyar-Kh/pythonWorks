from django.db import models

class Emplyee(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone=models.IntegerField()

    def __str__(self):
        return (f"{self.firstname} {self.lastname}")
    
class Student_tb(models.Model): 
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField()
    Address=models.TextField(null=True,blank=True)

