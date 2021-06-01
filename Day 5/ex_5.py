class Employee:
    name = "jevin"
    designation = "Web Developer"

class EmployeeField(Employee):
    salary = 54000

emp = EmployeeField
print("Employee details : \nName: ",emp.name,
      "\nDesignation: ",emp.designation,"\nsalary: ",emp.salary)