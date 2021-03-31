from django.db import models

# Create your models here.

class Signup(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=30)
    release_date = models.DateField()

class Technology(models.Model):
    # username=models.CharField(max_length=40)
    session=models.CharField(max_length=40,unique=True)
    
    def __str__(self):
        return self.session


class Student(models.Model):
    name=models.CharField(max_length=30, unique=False)
    session=models.ForeignKey("Technology", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

#Change the table name in admin(remove 's') --> verbose
#Write a ORM query to find out the username who attends Python session
#['','']

# Types of inheritance
# Django Abstract Base Class model inheritance
# Django Multi Table Model Inheritance

class Contactinfo(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=80)

    class Meta:
        abstract=True
# This is not used as a normal Django model


class Customer(Contactinfo):
    phone=models.CharField(max_length=30)

class Staff(Contactinfo):
    position=models.CharField(max_length=30)


class Place(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurant(Place):
    italian=models.BooleanField(default=False)
    chinese=models.BooleanField(default=False)

    def __str__(self):
        return self.italian
