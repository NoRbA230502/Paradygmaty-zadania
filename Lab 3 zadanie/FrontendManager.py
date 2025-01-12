from EmployeesManager import EmployeesManager


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def show_menu(self):
        while True:
            print("\n--- Employees System ---")
            print("1. Add new employee")
            print("2. Display all employees")
            print("3. Remove employees by age range")
            print("4. Find employee by name")
            print("5. Update employee salary")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_new_employee()
            elif choice == '2':
                self.display_all_employees()
            elif choice == '3':
                self.remove_employees_by_age_range()
            elif choice == '4':
                self.find_employee_by_name()
            elif choice == '5':
                self.update_employee_salary()
            elif choice == '6':
                print("Exiting system.")
                break
            else:
                print("Invalid choice, please try again.")

    def add_new_employee(self):
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        salary = float(input("Enter employee salary: "))
        self.manager.add_employee(name, age, salary)
        print("Employee added successfully.")

    def display_all_employees(self):
        self.manager.display_all_employees()

    def remove_employees_by_age_range(self):
        min_age = int(input("Enter minimum age: "))
        max_age = int(input("Enter maximum age: "))
        self.manager.remove_employees_by_age_range(min_age, max_age)

    def find_employee_by_name(self):
        name = input("Enter employee name to search: ")
        self.manager.find_employee_by_name(name)

    def update_employee_salary(self):
        name = input("Enter employee name to update salary: ")
        new_salary = float(input("Enter new salary: "))
        self.manager.update_employee_salary(name, new_salary)
