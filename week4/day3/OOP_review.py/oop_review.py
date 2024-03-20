import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# OOP: class, objects, attributes, methods, etc

# the constructor __init__, and attributes OK
# dunder methods OK
# encapsulation OK
# decorators OK
# methods OK
# inheritance 

#Best practice to organize classes:
# 1- __init__
# 2- dunder methods
# 3- decorators (@classmethod @static)
# 4- properties decorators @getters @setters @deleters.. other decorator
# 5- regular methods


class Employee:

    used_emails = set()


    def __init__(self, firstname, lastname, age, job, salary, address):  #attributes
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        self.salary = salary
        # self.email = f'{firstname.lower()}_{lastname.lower()}@company.com' #I dont need after creating the getter
        self.__address = address

    def __gt__(self, other):
        return self.salary > other.salary
    
    def __add__(self, other):
        result = self.salary + other.salary
        return result
    
    def __str__(self):
        return f'''
        full name: {self.get_fullname()}
        job: {self.job}
        email: {self.email}'''
    
    @classmethod
    def get_from_file(cls, file_name):
        with open(f'{dir_path}\\{file_name}', 'r') as file:
            data = json.load(file)
            return Employee(data['firstname'], data['lastname'],data['age'], data['job'], data['salary'], data['address'])

    @staticmethod
    def is_valid_email(email):
        return email in Employee.used_emails
           

    @property #getter
    def address(self):
        return self.__address
    
    @property #getter
    def email(self):
        email = f'{self.firstname.lower()}_{self.lastname.lower()}@company.com'
        if Employee.is_valid_email(email):
            Employee.used_emails.add(email)
            return email
        else:
            print('this email already exists')
    
    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @fullname.setter
    def fullname(self, new_name):
        first, last, third = new_name.split(' ')
        self.firstname = first
        self.lastname = last + third       
    
    def happy_birthday(self):
        self.age += 1
    
    def get_promotion(self, new_promotion) :
        self.salary += new_promotion


employee1 = Employee('John', 'Doe', 40, 'Front-end Developer', 30000, 'Avenida Paulista, 1120 - Sao Paulo')
employee2 = Employee('Jane', 'Austin', 30, 'Data Analyst', 40000, 'Rua dos Pinheiros, 55 - Sao Paulo')
employee3 = Employee.get_from_file('employees_info.json')
employee4 = Employee('Jane', 'Austin', 55, 'Project Manager', 20000, 'Rua dos Montes, 55 - Sao Paulo')

employee1.email
employee2.email
employee3.email
employee4.email

print(employee3.fullname)
print(Employee.used_emails)
# print(employee1.email)
# print(employee1.get_fullname())
# print(employee1.__dict__)
# employee1.get_promotion(5000)
# print(employee1.salary)

# print(employee1 < employee2)
# print(employee1 + employee2)
# print(employee1)

# print(employee1.address) #using @property I see the right output

# employee2.lastname = 'Silva'
# print(employee2.lastname)
# print(employee2.get_fullname())
# print(employee2.email)

# employee1.fullname = 'Ross Geller Silva'
# print(employee1.fullname)

###############   EXERCISE  #####################
# 1. Define Developer class inheriting from Employee
# 2. in a different file, import the Employee class and Define a new class named Developer that inherits from the Employee class.

# 3. Add additional attributes to the Developer class:
# programming_languages: a list to store the programming languages known by the developer.
# github_username: a string to store the developer's GitHub username.
# Implement a constructor (__init__ method) for the Developer class. The constructor should accept parameters for firstname, lastname, age, job, salary, address, programming_languages, and github_username, and initialize these attributes accordingly. Make use of the super() function to call the superclass constructor to initialize inherited attributes.

# 4. Implement a method named add_language(self, language) in the Developer class. This method should take a programming language as an argument and add it to the list of programming languages known by the developer.

# 5. Implement a method named show_languages(self) in the Developer class. This method should print out the list of programming languages known by the developer.

# 6. Implement a method named update_github_username(self, new_username) in the Developer class. This method should update the GitHub username of the developer with the provided new username.

# 7. Create an object of the Developer class and initialize it with appropriate values for all attributes, including inherited attributes from the Employee class.

# 8. Call the show_info() method inherited from the Employee class to display the basic information about the developer.

# 9. Call the add_language() method to add a few programming languages to the developer's skill set.

# 10. Call the show_languages() method to display the list of programming languages known by the developer.

# 11. Call the update_github_username() method to update the developer's GitHub username.

# Optionally, experiment with other methods inherited from the Employee class or define new methods specific to the Developer class.

#Finally, add doc strings in the whole code and organize your Developer class following the best practices for the order of the methods in both classes (Employee and Developer):

# Dunder (Magic) Methods: These special methods, such as __init__, __str__, __repr__, __add__, etc., should typically come first. They define how instances of your class behave in various contexts and are fundamental to understanding its behavior.

# Class Methods and Static Methods: These methods, which are decorated with @classmethod and @staticmethod respectively, should follow dunder methods. They provide additional functionalities related to the class or instance but are not dependent on specific instance data.

# Properties (Getters, Setters, Deleters): Methods decorated with @property, @<property>.setter, and @<property>.deleter should come next. These methods define how attributes are accessed, set, and deleted and are usually placed together for clarity.

# Regular Methods: These are the regular instance methods that perform various operations on instance data. They should come after properties and other special methods. Group related methods together to improve readability and maintainability.