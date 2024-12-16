# MCQ Answers

1. **Explain the following ways to print formatted output with the help of examples:**

   - **i) % Operator**
     ```python
     name = "Alice"
     age = 30
     print("Name: %s, Age: %d" % (name, age))
     ```
   - **ii) format() Method**
     ```python
     print("Name: {}, Age: {}".format(name, age))
     ```
   - **iii) f-string (Python 3.6+)**
     ```python
     print(f"Name: {name}, Age: {age}")
     ```

2. **Explain different mutable and immutable data types with examples.**

   - **Mutable Data Types**: These can be changed after creation.
     - Example: Lists, Dictionaries
     ```python
     my_list = [1, 2, 3]
     my_list[0] = 10  # List is mutable
     ```
   - **Immutable Data Types**: These cannot be changed after creation.
     - Example: Tuples, Strings
     ```python
     my_tuple = (1, 2, 3)
     # my_tuple[0] = 10  # This will raise an error
     ```

3. **Explain arithmetic operators and logical operators in Python. Write a Python program to demonstrate arithmetic and logical operators.**

   - **Arithmetic Operators**: +, -, \*, /, %, \*\* (exponentiation)
   - **Logical Operators**: and, or, not

   ```python
   a = 10
   b = 5
   print("Addition:", a + b)  # 15
   print("Logical AND:", (a > b) and (b > 0))  # True
   ```

4. **Explain different conditional statements in Python. Write a program to demonstrate the working of if-else statement.**

   - **Conditional Statements**: if, elif, else

   ```python
   num = 10
   if num > 0:
       print("Positive")
   elif num < 0:
       print("Negative")
   else:
       print("Zero")
   ```

5. **Differentiate between while and for loop. Provide syntax and examples of each.**

   - **While Loop**: Repeats as long as a condition is true.
     ```python
     i = 0
     while i < 5:
         print(i)
         i += 1
     ```
   - **For Loop**: Iterates over a sequence (like a list).
     ```python
     for i in range(5):
         print(i)
     ```

6. **Explain the use of the break, continue, and pass statements with examples.**

   - **break**: Exits the loop.
     ```python
     for i in range(5):
         if i == 3:
             break
         print(i)  # Prints 0, 1, 2
     ```
   - **continue**: Skips the current iteration.
     ```python
     for i in range(5):
         if i == 3:
             continue
         print(i)  # Prints 0, 1, 2, 4
     ```
   - **pass**: Does nothing; acts as a placeholder.
     ```python
     for i in range(5):
         if i == 3:
             pass  # Placeholder
         print(i)  # Prints 0, 1, 2, 3, 4
     ```

7. **Explain how to define a function in Python with the help of an example.**

   ```python
   def greet(name):
       return f"Hello, {name}!"

   print(greet("Alice"))  # Output: Hello, Alice!
   ```

8. **Explain positional and keyword arguments in Python functions with the help of an example.**

   - **Positional Arguments**: Arguments that need to be in the correct order.
   - **Keyword Arguments**: Arguments that are passed by explicitly stating the parameter name.

   ```python
   def describe_pet(animal_type, pet_name):
       print(f"I have a {animal_type} named {pet_name}.")

   describe_pet("hamster", "Harry")  # Positional
   describe_pet(pet_name="Willie", animal_type="dog")  # Keyword
   ```

9. **Explain how to define a function in Python with the help of an example. Explain variable length arguments in Python function with the help of an example.**

   ```python
   def add_numbers(*args):  # Variable length arguments
       return sum(args)

   print(add_numbers(1, 2, 3))  # Output: 6
   print(add_numbers(1, 2, 3, 4, 5))  # Output: 15
   ```

10. **Explain different ways to import a module in Python. Explain the following functions of the random module with the help of an example:**

    - **Importing a module**:
      ```python
      import random  # Import the whole module
      from random import randint  # Import specific function
      ```
    - **Functions**:
      - **random()**: Returns a random float between 0.0 to 1.0.
        ```python
        print(random.random())
        ```
      - **randint(a, b)**: Returns a random integer between a and b.
        ```python
        print(random.randint(1, 10))
        ```
      - **choice(seq)**: Returns a random element from a non-empty sequence.
        ```python
        print(random.choice(['apple', 'banana', 'cherry']))
        ```
      - **shuffle(lst)**: Shuffles the elements of a list in place.
        ```python
        my_list = [1, 2, 3, 4, 5]
        random.shuffle(my_list)
        print(my_list)
        ```

11. **WAP to demonstrate the following functions in the math module:**

    ```python
    import math

    print("Ceil:", math.ceil(4.2))  # 5
    print("Trunc:", math.trunc(4.9))  # 4
    print("Floor:", math.floor(4.9))  # 4
    print("Factorial:", math.factorial(5))  # 120
    print("Fabs:", math.fabs(-4.5))  # 4.5
    print("Pow:", math.pow(2, 3))  # 8.0
    print("Fmod:", math.fmod(5, 2))  # 1.0
    print("Fsum:", math.fsum([1, 2, 3, 4]))  # 10.0
    print("Sqrt:", math.sqrt(16))  # 4.0
    print("Prod:", math.prod([1, 2, 3, 4]))  # 24
    ```

12. **Explain string data type. Explain the following functions:**

    - **String Data Type**: A sequence of characters enclosed in quotes.

    ```python
    my_string = "Hello, World!"
    ```

    - **Functions**:
      - **lower()**: Converts to lowercase.
        ```python
        print(my_string.lower())  # hello, world!
        ```
      - **upper()**: Converts to uppercase.
        ```python
        print(my_string.upper())  # HELLO, WORLD!
        ```
      - **title()**: Converts to title case.
        ```python
        print(my_string.title())  # Hello, World!
        ```
      - **isupper()**: Checks if all characters are uppercase.
        ```python
        print(my_string.isupper())  # False
        ```
      - **count()**: Counts occurrences of a substring.
        ```python
        print(my_string.count("o"))  # 2
        ```

13. **Explain forward indexing and backward indexing in string with the help of an example. Describe Python's string slicing feature with examples.**

    - **Forward Indexing**: Starts from 0.
      ```python
      print(my_string[0])  # H
      ```
    - **Backward Indexing**: Starts from -1.
      ```python
      print(my_string[-1])  # !
      ```
    - **Slicing**: Extracts a substring.
      ```python
      print(my_string[0:5])  # Hello
      print(my_string[-6:])   # World!
      ```

14. **Explain List. Explain different ways to create a list in Python. Explain different ways to remove elements from list with the help of an example program.**

    - **List**: A mutable, ordered collection of items.

    ```python
    my_list = [1, 2, 3, 4, 5]
    ```

    - **Creating Lists**:
      ```python
      list1 = []  # Empty list
      list2 = list((1, 2, 3))  # From tuple
      ```
    - **Removing Elements**:
      ```python
      my_list.remove(3)  # Removes first occurrence of 3
      del my_list[0]  # Removes element at index 0
      my_list.pop()  # Removes last element
      ```

15. **What is a list comprehension? Write a program using list comprehension that generates a list of squares for numbers from 1 to 10.**

    - **List Comprehension**: A concise way to create lists.

    ```python
    squares = [x**2 for x in range(1, 11)]
    print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    ```

16. **Explain dictionary. Explain different ways to create a dictionary in Python. Explain how to retrieve all the keys, values, and key-value pairs in the dictionary.**

    - **Dictionary**: A mutable, unordered collection of key-value pairs.

    ```python
    my_dict = {'name': 'Alice', 'age': 30}
    ```

    - **Creating Dictionaries**:
      ```python
      dict1 = {}  # Empty dictionary
      dict2 = dict(name='Bob', age=25)  # Using dict()
      ```
    - **Retrieving Keys, Values, and Items**:
      ```python
      print(my_dict.keys())  # dict_keys(['name', 'age'])
      print(my_dict.values())  # dict_values(['Alice', 30])
      print(my_dict.items())  # dict_items([('name', 'Alice'), ('age', 30)])
      ```

17. **Explain set. How to create a set. Write a program to demonstrate the use of set operations (union, intersection, difference).**

    - **Set**: An unordered collection of unique items.

    ```python
    my_set = {1, 2, 3, 4}
    ```

    - **Set Operations**:

    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    print(set1.union(set2))  # {1, 2, 3, 4, 5}
    print(set1.intersection(set2))  # {3}
    print(set1.difference(set2))  # {1, 2}
    ```

18. **Explain tuple. How to create an empty tuple and a singleton tuple. Explain similarities and dissimilarities between list and tuple.**

    - **Tuple**: An immutable ordered collection.

    ```python
    empty_tuple = ()
    singleton_tuple = (1,)  # Note the comma
    ```

    - **Similarities**: Both can store multiple items and can be indexed.
    - **Dissimilarities**: Lists are mutable, while tuples are immutable.

19. **Explain array in Python. Explain the following with the help of an example:**

    - **Array**: A collection of items of the same type.

    ```python
    import array as arr
    my_array = arr.array('i', [1, 2, 3])  # 'i' indicates integer type
    ```

    - **Access Elements**:

    ```python
    print(my_array[0])  # 1
    ```

    - **Add Elements**:

    ```python
    my_array.append(4)
    ```

    - **Modify Elements**:

    ```python
    my_array[0] = 10
    ```

20. **Explain class and object. Write a program to create a class and object.**

    - **Class**: A blueprint for creating objects.
    - **Object**: An instance of a class.

    ```python
    class Dog:
        def bark(self):
            return "Woof!"

    my_dog = Dog()
    print(my_dog.bark())  # Woof!
    ```

21. **Explain constructor. Explain the concept of default constructor and parameterized constructor with the help of examples.**

    - **Constructor**: A special method that initializes an object.
    - **Default Constructor**:

    ```python
    class Person:
        def __init__(self):
            self.name = "Unknown"

    person1 = Person()
    print(person1.name)  # Unknown
    ```

    - **Parameterized Constructor**:

    ```python
    class Person:
        def __init__(self, name):
            self.name = name

    person2 = Person("Alice")
    print(person2.name)  # Alice
    ```

22. **Explain different types of variables that can be defined in a class in Python. Explain different ways to create an instance variable in Python in a class.**

    - **Types of Variables**:
      - **Instance Variables**: Unique to each instance.
      - **Class Variables**: Shared among all instances.

    ```python
    class MyClass:
        class_var = "I am a class variable"

        def __init__(self, instance_var):
            self.instance_var = instance_var  # Instance variable

    obj = MyClass("I am an instance variable")
    print(obj.instance_var)  # I am an instance variable
    print(MyClass.class_var)  # I am a class variable
    ```

23. **Explain inheritance. Explain hierarchical inheritance with the help of example program.**

    - **Inheritance**: A way to form new classes using classes that have already been defined.
    - **Hierarchical Inheritance**: Multiple subclasses inherit from a single superclass.

    ```python
    class Animal:
        def speak(self):
            return "Animal speaks"

    class Dog(Animal):
        def bark(self):
            return "Woof!"

    class Cat(Animal):
        def meow(self):
            return "Meow!"

    dog = Dog()
    cat = Cat()
    print(dog.speak())  # Animal speaks
    print(cat.speak())  # Animal speaks
    ```

24. **Explain single inheritance and multilevel inheritance with the help of example programs.**

    - **Single Inheritance**: A class inherits from one superclass.

    ```python
    class Parent:
        def greet(self):
            return "Hello!"

    class Child(Parent):
        def play(self):
            return "Playing!"

    child = Child()
    print(child.greet())  # Hello!
    ```

    - **Multilevel Inheritance**: A class inherits from a subclass.

    ```python
    class Grandparent:
        def greet(self):
            return "Hello from Grandparent!"

    class Parent(Grandparent):
        def greet(self):
            return "Hello from Parent!"

    class Child(Parent):
        def greet(self):
            return "Hello from Child!"

    child = Child()
    print(child.greet())  # Hello from Child!
    ```

25. **Explain different modes in which Python file can be opened. Write a program to write “Have a nice day” in a text file and read it.**

    - **Modes**:
      - `'r'`: Read (default)
      - `'w'`: Write (overwrites file)
      - `'a'`: Append
      - `'b'`: Binary mode
      - `'t'`: Text mode (default)

    ```python
    with open("example.txt", "w") as file:
        file.write("Have a nice day")

    with open("example.txt", "r") as file:
        content = file.read()
        print(content)  # Have a nice day
    ```

26. **Explain the following ways to read content of text file in Python with the help of an example:**

    - **read()**: Reads the entire file.

    ```python
    with open("example.txt", "r") as file:
        content = file.read()
    ```

    - **read(n)**: Reads the first n characters.

    ```python
    with open("example.txt", "r") as file:
        content = file.read(5)  # Reads first 5 characters
    ```

    - **readline()**: Reads the next line.

    ```python
    with open("example.txt", "r") as file:
        line = file.readline()  # Reads the first line
    ```

    - **readlines()**: Reads all lines into a list.

    ```python
    with open("example.txt", "r") as file:
        lines = file.readlines()  # List of lines
    ```

27. **Explain the following with respect to exception handling. Also, write a program to exhibit these concepts:**

    - **try**: Block of code to test for errors.
    - **except**: Block of code that executes if an error occurs.
    - **finally**: Block of code that executes regardless of an error.

    ```python
    try:
        x = 1 / 0  # This will raise an exception
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("This will always execute.")
    ```

28. **What is exception handling in Python? Write a program that demonstrates how to handle an exception.**

    - **Exception Handling**: A mechanism to handle runtime errors, allowing the program to continue running.

    ```python
    try:
        num = int(input("Enter a number: "))
        print(10 / num)
    except ValueError:
        print("Invalid input! Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    ```

29. **What is lambda in Python? Explain the rules for writing lambda along with its syntax and example.**

    - **Lambda**: An anonymous function defined with the `lambda` keyword.
    - **Syntax**: `lambda arguments: expression`

    ```python
    add = lambda x, y: x + y
    print(add(5, 3))  # Output: 8
    ```

30. **Explain the following widgets of tkinter with the help of example program:**

    - **Label**: Displays text or images.
    - **Entry**: A single-line text entry field.
    - **Button**: A clickable button.

    ```python
    import tkinter as tk

    def on_button_click():
        print("Button clicked!")

    root = tk.Tk()
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack()

    root.mainloop()
    ```
