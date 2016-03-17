from django.contrib import admin
from .models import Employee
# Register your models here.

class employeeAdmin(admin.ModelAdmin):
	list_display = ["employee_name", "employee_salary"]
	class meta:
		model = Employee,
admin.site.register(Employee)