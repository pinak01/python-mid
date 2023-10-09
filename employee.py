class employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
    def calc_emp_salary(self,working_hours):
        if working_hours>50: 
         overtime=working_hours-50
         self.emp_salary=self.emp_salary+(overtime*(self.emp_salary/50))
         return self.emp_salary
        else:
           return self.emp_salary
    def assign_department(self,new_department):
       self.emp_department=new_department
       return None
    def print_emp_details(self):
       print(self.emp_salary)
       print(self.emp_id)
       print(self.emp_name)
       print(self.emp_department)
       return None
emp1=employee("23BCE1253","PINAK DEBNATH",1500000,"Software Engineer")
print(emp1.calc_emp_salary(60))
print(emp1.assign_department("prompt engineer"))
print(emp1.print_emp_details())
print(employee.__dict__)
    


        