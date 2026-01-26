from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def home_view(request):  # home page
    employee = Employee.objects.all()
    print(Employee)
    
    return render(request, 'testapp/home.html', {'employee': employee})

from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# Fetch the employee details
def employee_detail_view(request, id):
    employee = get_object_or_404(Employee, id=id)
    # print("="*40)
    # print(employee) 
    # print("="*40)
    # return HttpResponse(employee) 
    return render(request, 'testapp/employee_detail.html', {'employee': employee})