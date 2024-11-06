# Submission Dates

- **Submission date for Elon Musk students**: 6 Nov 2024

## OOP

1. **Create a person class with:**

   - i) Two instance variables: `name`, `age`.
   - ii) Create a parameterized constructor.

   **Create a student class. Inherit person class in Student class.**

   - Student class should have:
     - i) Instance variables: `rollno` and `stream`.
     - ii) Create a parameterized constructor to initialize all instance variables of the student class as well as the Person class.
     - iii) Instance method: `display()` to print `name`, `age`, `rollno`, and `stream`.
   - Create an object of the Student class and call the `display` method.

2. **Write a Python class named Circle.**

   - Declare an instance variable, `radius`, and two methods that will compute the area and the perimeter of a circle.

3. **Write a Python program to create a calculator class.**

   - Include methods for basic arithmetic operations.

4. **Write a Python program to create a class representing a shopping cart.**

   - Include methods for adding and removing items, and calculating the total price.

5. **Write a Python class Employee with attributes like:**

   - `emp_id`, `emp_name`, `emp_salary`, and `emp_department`.
   - Methods like:
     - `calculate_emp_salary`
     - `emp_assign_department`
     - `print_employee_details`

   **Sample Employee Data:**

   - "ADAMS", "E7876", 50000, "ACCOUNTING"
   - "JONES", "E7499", 45000, "RESEARCH"
   - "MARTIN", "E7900", 50000, "SALES"
   - "SMITH", "E7698", 55000, "OPERATIONS"

   - Use `assign_department` method to change the department of an employee.
   - Use `print_employee_details` method to print the details of an employee.
   - Use `calculate_emp_salary` method that takes two arguments: `salary` and `hours_worked`, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as follows:
     - `overtime = hours_worked - 50`
     - `Overtime amount = (overtime * (salary / 50))`

6. **Write a Python class BankAccount with attributes like:**

   - `account_number`, `balance`, `date_of_opening`, and `customer_name`.
   - Methods like:
     - `deposit`
     - `withdraw`
     - `check_balance`

7. **Create a class hierarchy for different types of geometric shapes, including circles, rectangles, and triangles, using inheritance.**
   - **Tasks:**
     - A. Define a base class called `Shape` with common attributes like `colour` and `area`.
     - B. Implement subclasses for specific shape types such as `Circle`, `Rectangle`, and `Triangle`. Each subclass should inherit from the `Shape` class.
     - C. Incorporate additional attributes and methods specific to each shape type. For example, a `Circle` class might have attributes like `radius` and methods like `calculate_area`.
     - D. Use inheritance to create subclasses representing variations within each shape type. For example, within the `Rectangle` class, create subclasses for `Square` and `Parallelogram`.
     - E. Implement methods or attributes in the subclasses to demonstrate how inheritance allows for the sharing of attributes and methods from parent classes.
     - F. Create instances of the various shape classes and test their functionality to ensure that attributes and methods work as expected.

## File Handling

8. **WAP to find the number of words in the given text file.**

   - **Hints**: Use the `split()` method to separate words.

9. **Write a program to write “Happy Programming” in a text file and read it.**

10. **WAP to demonstrate the working of the following functions:**

    - i) `read()`
    - ii) `read(n)`
    - iii) `readline()`
    - iv) `readlines()`

11. **WAP that exhibits the working of the following functions:**

    - i) `write()`
    - ii) `writelines()`

12. **Write a Python program to read the first n lines of a file.**

13. **Write a Python program to append text to a file and display the text.**

14. **Write a Python program to read the last n lines of a file.**

15. **Write a Python program to read a file line by line and store it into a list.**

## Exception Handling

16. **Write a program to exhibit these concepts:**

    - i) `try`
    - ii) `except`
    - iii) `finally`

17. **Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.**

18. **Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.**

19. **WAP that exhibits multiple except blocks along with a default block.**

20. **WAP that exhibits except blocks that can catch multiple exceptions.**

## Lambda

21. **WAP to demonstrate how to use lambda in `map()` function.**

22. **WAP to demonstrate how to use lambda in `filter()` function.**

23. **Write a Python program to filter a list of integers into a list of even numbers and a list of odd numbers using Lambda.**

    - **Hint**: Use lambda in `filter()`.

24. **Write a Python program to square and cube every number in a given list of integers using Lambda.**

    - **Hint**: Use lambda in `map()`.

25. **Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument.**

26. **Create a lambda function that multiplies argument x with argument y and prints the result.**
