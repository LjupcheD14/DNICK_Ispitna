from django.contrib import admin
from .models import Restaurant, Dish, DishRestaurant, Employee, BusinessHours
# Register your models here.


admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(DishRestaurant)
admin.site.register(Employee)