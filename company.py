from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for employee in self.employees:
            print(employee.fname, employee.lname)
        print('----------------------------')

    def pay_employees(self):
        print("Paying Employees:")
        for employee in self.employees:
            print("Paycheck for:", employee.fname, employee.lname)
            print(f"Amount:, {employee.calculate_paycheck():,.2f}")
        print('----------------------------------')

    
def main():
    my_company = Company()
    my_company.add_employee(SalaryEmployee("John", "Doe", 50000))
    my_company.add_employee(HourlyEmployee("Janet", "Doe", 20, 50))
    my_company.add_employee(CommissionEmployee("Jack", "Doe", 120000, 5, 2000))
   
    my_company.display_employees()
    my_company.pay_employees()
    
main()