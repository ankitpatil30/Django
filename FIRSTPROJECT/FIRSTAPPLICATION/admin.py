from django.contrib import admin
from FIRSTAPPLICATION.models import Signup, Technology, Student, Customer, Staff, Place, Restaurant

# Register your models here.

admin.site.register(Signup)
admin.site.register(Technology)
admin.site.register(Student)

admin.site.register(Customer)
admin.site.register(Staff)

admin.site.register(Place)
admin.site.register(Restaurant)
