from Employee import Employee


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        new_employee = Employee(name, age, salary)
        self.employees.append(new_employee)

    def display_all_employees(self):
        if not self.employees:
            print("No employees to display.")
        for emp in self.employees:
            print(emp)

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        print(f"Employees aged between {min_age} and {max_age} have been removed.")

    def find_employee_by_name(self, name):
        found_employees = [emp for emp in self.employees if name.lower() in emp.name.lower()]
        if found_employees:
            for emp in found_employees:
                print(emp)
        else:
            print("No employee found with that name.")

    def update_employee_salary(self, name, new_salary):
        for emp in self.employees:
            if name.lower() == emp.name.lower():
                emp.update_salary(new_salary)
                print(f"Salary of {emp.name} updated to {new_salary}.")
                return
        print("Employee not found.")
