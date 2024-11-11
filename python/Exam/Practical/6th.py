#Design a simple student information system using classes and inheritance
# Student Information System

class Person:
    """Base class for a person."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        """Display basic information about the person."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    """Derived class for a student."""
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)  # Call the constructor of the base class
        self.student_id = student_id
        self.course = course

    def display_info(self):
        """Display information about the student, including inherited info."""
        super().display_info()  # Call the base class method
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

def main():
    """Main function to run the Student Information System."""
    print("Welcome to the Student Information System")

    # Create a student object
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    student_id = input("Enter student ID: ")
    course = input("Enter course: ")

    student = Student(name, age, student_id, course)

    # Display student information
    print("\nStudent Information:")
    student.display_info()

if __name__ == "__main__":
    main()