class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary
