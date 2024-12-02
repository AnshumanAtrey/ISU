# Practical Programming Tasks

1. **WAP to demonstrate arithmetic operators.**

   ```python
   a = 10
   b = 5
   print("Addition:", a + b)        # 15
   print("Subtraction:", a - b)     # 5
   print("Multiplication:", a * b)  # 50
   print("Division:", a / b)        # 2.0
   print("Modulus:", a % b)         # 0
   print("Exponentiation:", a ** b) # 100000
   ```

2. **WAP to find the greatest number among three numbers.**

   ```python
   def greatest_number(x, y, z):
       return max(x, y, z)

   print("Greatest number is:", greatest_number(10, 20, 15))  # 20
   ```

3. **WAP to add numbers from 5 to 15 using a for loop.**

   ```python
   total = 0
   for i in range(5, 16):
       total += i
   print("Sum from 5 to 15 is:", total)  # 105
   ```

4. **WAP to find the factorial of a number.**

   ```python
   def factorial(n):
       if n == 0:
           return 1
       else:
           return n * factorial(n - 1)

   print("Factorial of 5 is:", factorial(5))  # 120
   ```

5. **WAP to print the following patterns:**

   ```
   *
   * *
   * * *
   ```

   ```python
   for i in range(1, 4):
       print('* ' * i)
   ```

6. **WAP to calculate sum and average of a given array: arr=('i',[1,2,3,4,5]).**

   ```python
   arr = [1, 2, 3, 4, 5]
   total = sum(arr)
   average = total / len(arr)
   print("Sum:", total)        # 15
   print("Average:", average)  # 3.0
   ```

7. **Create a function to check whether a number is prime or not.**

   ```python
   def is_prime(n):
       if n <= 1:
           return False
       for i in range(2, int(n**0.5) + 1):
           if n % i == 0:
               return False
       return True

   print("Is 11 prime?", is_prime(11))  # True
   ```

8. **Create a recursive function to print Fibonacci series up to 10 terms.**

   ```python
   def fibonacci(n):
       if n <= 0:
           return []
       elif n == 1:
           return [0]
       elif n == 2:
           return [0, 1]
       else:
           fib_series = fibonacci(n - 1)
           fib_series.append(fib_series[-1] + fib_series[-2])
           return fib_series

   print("Fibonacci series up to 10 terms:", fibonacci(10))
   ```

9. **WAP to check whether the string is palindrome or not.**

   ```python
   def is_palindrome(s):
       return s == s[::-1]

   print("Is 'radar' a palindrome?", is_palindrome("radar"))  # True
   ```

10. **WAP to create a user-defined function to calculate the sum of variable number of arguments using the concept of variable length argument in function.**

    ```python
    def sum_of_numbers(*args):
        return sum(args)

    print("Sum of numbers:", sum_of_numbers(1, 2, 3, 4, 5))  # 15
    ```

11. **Write a Python program to remove duplicates from a list.**

    ```python
    my_list = [1, 2, 2, 3, 4, 4, 5]
    unique_list = list(set(my_list))
    print("List after removing duplicates:", unique_list)  # [1, 2, 3, 4, 5]
    ```

12. **WAP to calculate the square of a number from 1 to 10 using list comprehension.**

    ```python
    squares = [x**2 for x in range(1, 11)]
    print("Squares from 1 to 10:", squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

13. **Write a Python program to compute the element-wise sum of given tuples.**

    ```python
    tuple1 = (1, 2, 3, 4)
    tuple2 = (3, 5, 2, 1)
    tuple3 = (2, 2, 3, 1)

    elementwise_sum = tuple(a + b + c for a, b, c in zip(tuple1, tuple2, tuple3))
    print("Element-wise sum of the said tuples:", elementwise_sum)  # (6, 9, 8, 6)
    ```

14. **WAP to get only unique items from two sets.**

    ```python
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    unique_items = set1.union(set2)
    print("Unique items from both sets:", unique_items)  # {1, 2, 3, 4, 5, 6}
    ```

15. **Use dictionary comprehension to create a dictionary to store only key-value pairs having even age.**

    ```python
    original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
    even_age_dict = {name: age for name, age in original_dict.items() if age % 2 == 0}
    print("Dictionary with even ages:", even_age_dict)  # {'jack': 38, 'michael': 48}
    ```

16. **WAP to remove spaces from the given string: “Python is very easy”.**

    ```python
    my_string = "Python is very easy"
    no_spaces = my_string.replace(" ", "")
    print("String without spaces:", no_spaces)  # Pythonisveryeasy
    ```

17. **WAP to input principle_amount, rate, time from the user. Calculate simple interest and print the value of simple interest using the format function.**

    ```python
    principle_amount = float(input("Enter principle amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))
    simple_interest = (principle_amount * rate * time) / 100
    print("Simple Interest: {:.2f}".format(simple_interest))
    ```

18. **Write a Python class named Circle. Declare an instance variable, radius, and two methods that will compute the area and the perimeter of a circle.**

    ```python
    import math

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return math.pi * (self.radius ** 2)

        def perimeter(self):
            return 2 * math.pi * self.radius

    circle = Circle(5)
    print("Area of circle:", circle.area())  # Area
    print("Perimeter of circle:", circle.perimeter())  # Perimeter
    ```

19. **Create a person class with:**

    - **i)** Two instance variables: name, age.
    - **ii)** Create a parameterized constructor.
    - **iii)** Create a student class that inherits from the person class.
    - **iv)** The student class has instance variables: rollno and stream.
    - **v)** Create a parameterized constructor to initialize all instance variables of the student class as well as the person class.
    - **vi)** Instance method: display() to print name, age, rollno, and stream.

    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, rollno, stream):
            super().__init__(name, age)
            self.rollno = rollno
            self.stream = stream

        def display(self):
            print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}, Stream: {self.stream}")

    student = Student("Alice", 20, "S123", "Computer Science")
    student.display()
    ```

20. **WAP to count the number of words in a text file.**

    ```python
    with open("example.txt", "r") as file:
        content = file.read()
        word_count = len(content.split())
    print("Number of words in the file:", word_count)
    ```

21. **WAP to handle ZeroDivisionError gracefully using exception handling.**

    ```python
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    ```

22. **WAP to demonstrate how to use lambda in map() function.**

    ```python
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, numbers))
    print("Squares:", squares)  # [1, 4, 9, 16, 25]
    ```

23. **WAP to demonstrate how to use lambda in filter() function.**

    ```python
    numbers = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("Even numbers:", evens)  # [2, 4, 6]
    ```

24. **WAP to demonstrate how to define class method and static method in a class.**

    ```python
    class MyClass:
        class_variable = "I am a class variable"

        @classmethod
        def class_method(cls):
            return cls.class_variable

        @staticmethod
        def static_method():
            return "I am a static method"

    print(MyClass.class_method())  # I am a class variable
    print(MyClass.static_method())  # I am a static method
    ```

25. **Create a GUI application to add two numbers using Label, Entry, and Button widgets.**

    ```python
    import tkinter as tk

    def add_numbers():
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")

    root = tk.Tk()
    root.title("Add Two Numbers")

    label1 = tk.Label(root, text="Number 1:")
    label1.pack()
    entry1 = tk.Entry(root)
    entry1.pack()

    label2 = tk.Label(root, text="Number 2:")
    label2.pack()
    entry2 = tk.Entry(root)
    entry2.pack()

    add_button = tk.Button(root, text="Add", command=add_numbers)
    add_button.pack()

    result_label = tk.Label(root, text="Result:")
    result_label.pack()

    root.mainloop()
    ```
