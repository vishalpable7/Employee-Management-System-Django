from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.location}"

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Emplyoee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,related_name="emp_dept")
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,related_name="emp_role")
    phone = models.IntegerField(default=0)
    hire_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"