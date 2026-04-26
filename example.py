

# def length_of_string(s):
#     count = 0
#     for _ in s:
#         count += 1
#     return count

# value = length_of_string("Hello, World!")
# value = length_of_string("Another string to test.")

# print(value)


# def length_of_string(s="codenetra"):
#     if s is None:
#         return 0
#     count = 0
#     for _ in s:
#         count += 1
#     return count

# print(length_of_string("this is an example string"))  # This will return the length of the string

# def min_max(numbers):
#     return min(numbers), max(numbers)


# numbers = [3, 1, 4, 1, 5, 9]
# minimum, maximum = min_max(numbers)
# print(f"Minimum: {minimum}, Maximum: {maximum}")

# def arugument(a, b=None, *args):
#     print(f"Argument 0: {a}")
#     print(f"Argument 1: {b}")
#     for i, arg in enumerate(args):
#         print(f"Argument {i}: {arg}")

# arugument(1, 2, 3, "hello", [4, 5, 6])

# def keywrord_arguments(*args, **kwargs):
#     print("Positional arguments:")
#     for i, arg in enumerate(args):
#         print(f"Argument {i}: {arg}")
#     print("Keyword arguments:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# keywrord_arguments((1, 2, 3, 4), a=1, b=2, c=3)


# def square(x):
#     return x * x

# square = lambda x: x * x
# print(square(5))  # Output: 25



# def add(x, y):
#     """
#     This function takes two numbers and returns their sum.
    
#     Parameters:
#     x (int or float): The first number.
#     y (int or float): The second number.

#     Returns:
#     int or float: The sum of x and y.

#     """
#     return x + y

# print(help(len))

# add(3, 4)  # Output: 7

# x = 10  # This is a global variable
# def scoper_checker():
#     # x = 10  # This is a local variable
#     print(f"Inside the function, x = {x}")

# def scoper_checker_2():
#     y = 20  # This is a local variable
#     print(f"Inside scoper_checker_2, x = {x}")
#     print(f"Inside scoper_checker_2, y = {y}")

# scoper_checker()
# scoper_checker_2()

# print(f"Outside the function, x = {x}")
# print(f"Outside the function, y = {y}")

# def global_variable_example():
#     global x  # Declare x as a global variable
#     x = 10  # This will modify the global variable x
#     print(f"Inside the function, x = {x}")

# def  global_variable_example_2():
#     print(f"Inside global_variable_example_2, x = {x}")  # This will access the global variable x

# global_variable_example()
# print(f"After calling the function, x = {x}")  # This will print the

# def local_Scope():
#     global count  # Declare count as a global variable
#     count = 0  # This will create a global variable count
    
#     print(f"Inside the function, count = {count}")

# local_Scope()
# print(f"Outside the function, count = {count}")  # This will raise an error because count is not defined outside the function


# try:
#     # result = 10 / 0  # This will raise a ZeroDivisionError
#     r1 = 10 + 5  # This will raise a TypeError
# except Exception as e:
#     print(f"Exception occurred: {e}")
# # except TypeError as e:
# #     print(f"TypeError occurred: {e}")
# finally:
#     print("This block will always execute, regardless of whether an exception occurred or not.")

# result = 10 / 0  # This will raise a ZeroDivisionError


# try:
#     result = 10 / 0  # This will raise a ZeroDivisionError
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     print("This block will always execute, regardless of whether an exception occurred or not.")


# def checker():
#     print("This is a checker function.")

# checker()

# with open("notes.txt", "w") as file:
#     file.write("This is a sample note.")
#     file.write("\nThis is another line in the note.")


# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("notes.txt", "a") as file:
#     file.write("\nThis line is appended to the note.")

# with open("notes.txt", "r") as file:
#     content = file.readlines()
#     for cont in content:
#         print(cont.strip())



# import json

# data = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York"
# }

# with open("data.json", "w") as json_file:
#     json.dump(data, json_file)

# with open("data.json", "r") as json_file:
#     loaded_data = json.load(json_file)
#     print(type(loaded_data))  # Output: dict
#     for key, value in loaded_data.items():
#         print(f"{key}: {value}")
#     print(loaded_data)


# from reader.read import reading_text
# text_content = reading_text(file_path="notes.txt")
# print(text_content)


# import math

# print(math.sqrt(16))  # Output: 4.0
# print(math.pi)  # Output: 3.141592653589793
# print(math.sin(math.pi / 2))  # Output: 1.0

# import random 
# print(random.randint(1, 10))  # Output: A random integer between 1 and 10
# print(random.random())  # Output: A random float between 0.0 and 1.0
# print(random.choice(['apple', 'banana', 'cherry']))  # Output: Randomly selects one of the fruits from the list

# list_of_numbers = [random.randint(1, 100) for _ in range(10)]

# print(list_of_numbers)


# from datetime import datetime
# print(datetime.now())  # Output: Current date and time
# print(datetime(2022, 1, 1))  # Output: 2022
# print(datetime.strptime("2022-01-01", "%Y-%m-%d"))
# print(datetime.now().strftime("%d/%m/%Y"))  # Output: 2022-01-01 00:00:00

# class Dog:
#     def __init__(self, name): #contructor method of the class Dog, which is called when an object of the class is created
#         self.name = None

#     def bark(self, name): #method definition inside the class Dog
#         self.name = name
#         return f"{name} says Woof!"
    
#     def name_dog(self):
#         return f"{self.name} is the name of the dog."
    
# my_dog = Dog() #creating object of the class Dog
# my_dog1 = Dog() #creating another object of the class Dog
# print(my_dog.bark("Buddy"))  # method call on the object my_dog, which will return "Buddy says Woof!"
# print(my_dog.name_dog())  # method call on the object my_dog, which will return "Buddy is the name of the dog."
# # print(my_dog.name)  # Accessing the name attribute of the my_dog object, which will return "Buddy"
# # print(my_dog1.bark())  # method call on the object my_dog1, which will return "Max says Woof!"
# # print(my_dog1.name)  # Accessing the name attribute of the my_dog1 object, which will return "Max"


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         return f"{self.name} is eating."
    
#     def sleep(self):
#         return f"{self.name} is sleeping."
    

# class Dog(Animal):
#     def bark(self):
#         return f"{self.name} says Woof!"
    
#     def eat(self):
#         return f"{self.name} is eating dog food."
    
# class Cat(Animal):
#     def meow(self):
#         return f"{self.name} says Meow!"
    
#     def eat(self):
#         return f"{self.name} is eating cat food."

# my_dog = Dog("Buddy")
# my_cat = Cat("Whiskers")

# print(my_dog.eat())  # Output: Buddy is eating dog food.
# print(my_dog.sleep())  # Output: Buddy is sleeping.
# print(my_dog.bark())  # Output: Buddy says Woof!

# print(my_cat.eat())  # Output: Whiskers is eating cat food.
# print(my_cat.sleep())  # Output: Whiskers is sleeping.
# print(my_cat.meow())  # Output: Whiskers says Meow!

# from reader.read import Person

# class Student(Person):
#     def __init__(self, name, age, student_id, major):
#         """Initialize the Student class, which inherits from the Person class."""
#         super().__init__(name, age)  # Call the constructor of the parent class (Person)
#         self.student_id = student_id
#         self.major = major

#     def study(self):
#         """Method for the Student class that returns a string indicating what the student is studying."""
#         return f"{self.name} is studying {self.major} {A}."
    

# class Employee(Person):
#     def __init__(self, name, age, employee_id, company):
#         super().__init__(name, age)  # Call the constructor of the parent class (Person)
#         self.employee_id = employee_id
#         self.company = company

#     def work(self):
#         return f"{self.name} is working at {self.company}."
    

# employee = Employee("Alice", 30, "E123", "Tech Company")
# print(employee.name)  # Output: Alice
# print(employee.age)  # Output: 30
# print(employee.employee_id)  # Output: E123
# print(employee.company)  # Output: Tech Company
# print(employee.work())  # Output: Alice is working at Tech Company.

# student = Student("Bob", 20, "S456", "Computer Science")
# print(student.name)  # Output: Bob
# print(student.age)  # Output: 20 
# print(student.student_id)  # Output: S456
# print(student.major)  # Output: Computer Science
# print(student.study())  # Output: Bob is studying Computer Science.


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # Using a single underscore to indicate that this attribute is intended to be private
        
#     def deposit(self, amount):
#         self.__balance += amount
#         return f"{amount} deposited. New balance: {self.__balance}"
    
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             return "Insufficient funds."
#         self.__balance -= amount
#         return f"{amount} withdrawn. New balance: {self.__balance}"
    
#     def __get_balance(self):
#         return self.__balance
    
# account = BankAccount("Alice", 1000)
# print(account.deposit(500))  # Output: 500 deposited. New balance: 150
# print(account.withdraw(200))  # Output: 200 withdrawn. New balance: 1300
# print(account.withdraw(2000))  # Output: Insufficient funds.
# print(account.owner)  # Output: Alice

# # print(account.__balance)  # This will raise an AttributeError because __balance is a private attribute
# # print(account.__get_balance())  # This will also raise an AttributeError because __get