from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from .models import Emplyoee, Department, Role
from datetime import datetime
from django.db.models import Q

def index(request):
        return render(request, "index.html")
    
def all_emp(request):
    queryset = Emplyoee.objects.all()
    context = {"emps":queryset}
    return render(request, "all_emp.html", context)
    
def add_emp(request):
    if request.method == "POST":
        f_name = request.POST['first_name']
        l_name = request.POST.get('last_name')
        salary = request.POST.get("emp_salary")
        dept = request.POST.get('emp_dept')
        role = request.POST.get('emp_role')
        phone = request.POST.get('emp_phone')
        bonus = request.POST.get('emp_bonus')
        Emplyoee.objects.create(first_name =f_name, last_name =l_name, dept_id =dept , salary = salary, bonus = bonus, role_id = role, phone= phone, hire_date = datetime.now())
        return HttpResponse("User added successfully")
    elif request.method == "GET":
        return render(request, "add_emp.html")
    else:
          HttpResponse("invalid request")

def update_emp(request,emp_id):
    if request.method == "GET":
        if emp_id:
            queryset = Emplyoee.objects.get(id = emp_id)
            context = {"emp":queryset}
            return render(request, "update_emp.html",context)
        
    if request.method == "POST":
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        salary = request.POST.get("emp_salary")
        dept_id = request.POST.get("emp_dept")
        role_id = request.POST.get("emp_role")
        phone = request.POST.get("emp_phone")
        location = request.POST.get("emp_location")
        bonus = request.POST.get("emp_bonus")
        try:
            emp_obj = Emplyoee.objects.get(id=emp_id)
            emp_obj.first_name = fname
            emp_obj.last_name = lname
            emp_obj.salary = salary
            emp_obj.dept.id = dept_id
            emp_obj.role.id = role_id
            emp_obj.phone = phone
            emp_obj.dept.location = location
            emp_obj.bonus = bonus
            emp_obj.dept.save()
            emp_obj.save()
            
            queryset = Emplyoee.objects.all()
            context = {"emps":queryset}
            return render(request, "all_emp.html", context)
        except:
            return HttpResponse("please enter valid data")
    else:
        return HttpResponse("invalid request")
    
    
def remove_emp(request):

        emps = Emplyoee.objects.all()
        context = {
              "emps":emps
        }
        return render(request, "remove_emp.html", context)

def remove_emp_id(request,emp_id):
        try:
            obj = Emplyoee.objects.get(id =emp_id)
            obj.delete()
            emps = Emplyoee.objects.all()
            context = {"emps":emps}
            return render(request, "remove_emp.html", context)
        except:
            return HttpResponse("Please choose the valid employee")

    
def filter_emp(request):

    if request.method == "POST":
        name = request.POST.get('first_name')
        role = request.POST.get('emp_role')
        dept = request.POST.get('emp_dept')
        emps = Emplyoee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains=name))
        if role:
            emps = emps.filter(role__name__icontains = role)
        if dept:
            emps = emps.filter(dept__name__icontains = dept)

        context = {"emps":emps}
        return render(request, "all_emp.html", context)
    
    elif request.method == "GET":
        return render(request, "filter_emp.html" )
    else:
        return HttpResponse("An exception occured")


