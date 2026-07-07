#Employee Management System


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")
        
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")

    def remove_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                self.employees.remove(employee)
                print(f"Employee {name} removed successfully.")
                return
        print(f"Employee {name} not found.")

    def display_all_employees(self):
        if not self.employees:
            print("No employees to display.")
            return
        for employee in self.employees:
            employee.display_info()
            print("-" * 20)
            
main_menu = """Employee Management System
1. Add Employee
2. Remove Employee
3. Display All Employees
4. Exit
"""
def main():
    system = EmployeeManagementSystem()
    
    while True:
        print(main_menu)
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, position, salary)
            system.add_employee(employee)
        
        elif choice == '2':
            name = input("Enter the name of the employee to remove: ")
            system.remove_employee(name)
        
        elif choice == '3':
            system.display_all_employees()
        
        elif choice == '4':
            print("Exiting the Employee Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()