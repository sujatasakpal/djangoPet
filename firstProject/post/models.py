from django.db import models

# Create your models here.

class Post(models.Model) :
    username =models.CharField(max_length=20)
    description=models.TextField()
    comment=models.CharField(max_length=50, default="This is a comment")


    def __str__(self):
        return self.username

class Student(models.Model):
    student_name=models.CharField(max_length=40)
    school_name=models.CharField(max_length=40)
