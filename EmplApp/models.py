from django.db import models

class Departments(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField("Имя сотрудника", max_length=500)
    Department=models.CharField("Департамент", max_length=500)
    DateOfJoining=models.DateField("Дата начала работы")
    PhotoFileName=models.CharField("Фото", max_length=500)
