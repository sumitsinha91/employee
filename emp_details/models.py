from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
	employee_name = models.CharField(max_length=200)
	employee_salary = models.CharField(max_length=90)

	def __str__(self):
		return self.employee_name
	