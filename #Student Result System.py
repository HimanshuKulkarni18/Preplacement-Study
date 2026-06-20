#Student Result System

class Student:
    def __init__(self, roll_no, name, math, science, english):
        self.roll_no = roll_no
        self.name = name
        self.marks = {
            'Math': math,
            'Science': science,
            'English': english
        }
        self.total = sum(self.marks.values())
        self.percentage = (self.total / 300) * 100
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 80:
            return 'A'
        elif self.percentage >= 70:
            return 'B'
        elif self.percentage >= 60:
            return 'C'
        elif self.percentage >= 40:
            return 'D'
        else:
            return 'Fail'

class ResultSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        print("\n--- Add Student Record ---")
        try:
            roll_no = input("Enter Roll Number: ").strip()
            if roll_no in self.students:
                print("Error: Roll number already exists!")
                return
            
            name = input("Enter Student Name: ").strip()
            math = float(input("Enter Math Marks (out of 100): "))
            science = float(input("Enter Science Marks (out of 100): "))
            english = float(input("Enter English Marks (out of 100): "))
            
            # Validate input ranges
            if not all(0 <= m <= 100 for m in [math, science, english]):
                print("Error: Marks must be between 0 and 100.")
                return

            student = Student(roll_no, name, math, science, english)
            self.students[roll_no] = student
            print(f"Record successfully added for {name}!")
        except ValueError:
            print("Invalid input! Marks must be numerical values.")

    def display_all(self):
        print("\n--- All Student Results ---")
        if not self.students:
            print("No records found.")
            return
        
        for roll_no, s in self.students.items():
            print(f"Roll No: {s.roll_no} | Name: {s.name} | Total: {s.total}/300 | "
                  f"Percentage: {s.percentage:.2f}% | Grade: {s.grade}")

    def search_student(self):
        print("\n--- Search Student ---")
        roll_no = input("Enter Roll Number to search: ").strip()
        student = self.students.get(roll_no)
        
        if student:
            print(f"\nResult Card for {student.name}:")
            print(f"Roll Number: {student.roll_no}")
            print("-" * 30)
            for subject, marks in student.marks.items():
                print(f"{subject}: {marks}/100")
            print("-" * 30)
            print(f"Total Marks: {student.total}/300")
            print(f"Percentage:  {student.percentage:.2f}%")
            print(f"Final Grade: {student.grade}")
        else:
            print("Student record not found.")

    def delete_student(self):
        print("\n--- Delete Student Record ---")
        roll_no = input("Enter Roll Number to delete: ").strip()
        if roll_no in self.students:
            del self.students[roll_no]
            print("Record deleted successfully.")
        else:
            print("Record not found.")

def main():
    system = ResultSystem()
    while True:
        print("\n==============================")
        print(" STUDENT RESULT SYSTEM")
        print("==============================")
        print("1. Add Student Record")
        print("2. Display All Results")
        print("3. Search Individual Result")
        print("4. Delete Student Record")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.display_all()
        elif choice == '3':
            system.search_student()
        elif choice == '4':
            system.delete_student()
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please type a number from 1 to 5.")

if __name__ == '__main__':
    main()

