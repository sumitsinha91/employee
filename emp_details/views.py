from django.shortcuts import render
# from django.views import generic 
from emp_details.models import Employee
# Create your views here.
def emp_details(request):
	if request.method == 'POST':	
		print request.POST
		name = request.POST['employeename']
		salary = request.POST['employeesalary']
		result=Employee(employee_name=name, employee_salary=salary)
		result.save()
		print request.POST
		# variable = Employee.objects.all()
		# return render(request, 'emp_details.html',{'variable':variable})
		return render(request, 'employee.html',{"name":name,"salary":salary})
	elif request.method == 'GET':
		pass
	return render(request, "emp_details.html", {})

def details(request):
	emp= Employee.objects.all()
	print (emp)
	return render(request, 'list.html', {'emp':emp})






