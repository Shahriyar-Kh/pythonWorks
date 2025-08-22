from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe_tb(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    Recipe_Name=models.CharField(max_length=100)
    Recipe_Description=models.TextField()
    Recipe_Image=models.ImageField(upload_to="Recipe_img")


class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering=["department"]

class Student_ID(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
class Student_Data(models.Model):
    dep=models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    student_id=models.OneToOneField(Student_ID,related_name="Studentid",on_delete=models.CASCADE)
    student_Name=models.CharField(max_length=100)
    student_Email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_add=models.TextField()

    def __str__(self) -> str:
        return self.student_Name
    
    class Mete:
        ordering=["student_Name"]
        verbose_name=["Student_Data"]
