from django.db import models

# Create your models here.

class Signup(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=30)
    release_date = models.DateField()

class Technology(models.Model):
    session=models.CharField(max_length=40,unique=True)
    
    def __str__(self):
        return self.session


class Student(models.Model):
    name=models.CharField(max_length=30, unique=False)
    session=models.ForeignKey("Technology", on_delete=models.PROTECT)

    def __str__(self):
        return self.name
