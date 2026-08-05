
          ##Q1###

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Sum =", a + b)
#     print("product",a*b)
#     print("remainder",a%b)
# except ValueError:
#     print("Invalid Data Type")
   
         ###Q2###

# ch = input("Enter a character: ")
# if ch.isupper():
#     print("Uppercase Letter")
# elif ch.islower():
#     print("Lowercase Letter")
# elif ch.isdigit():
#     print("Digit")
# else:
#     print("Special Character")

   
       #######Q3#####

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)

     ##########Q7######

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient Balance")
#     def display(self):
#         print("Balance =",self.balance)
# name = input("Name: ")
# balance = float(input("Balance: "))
# b = BankAccount(name, balance)
# d = float(input("Deposit: "))
# b.deposit(d)
# w = float(input("Withdraw: "))
# b.withdraw(w)
# b.display()
        

#########Q5######

# class Rectangle:
#     def __init__(self, l, b):
#         self.length = l
#         self.breadth = b
#     def area(self):
#         print("Area =", self.length*self.breadth)
# l = int(input("Length: "))
# b = int(input("Breadth: "))
# r = Rectangle(l, b)
# r.area()

########Q4#######

# n = int(input("Enter a number: "))
# count=0
# while n>0:
#     count += 1
#     n=n//10
# print("Digits =",count)


##########Q6########

# filename = input("Enter filename: ")
# try:
#     with open(filename, "r") as f:
#         data = f.read()
#     print("Lines =", len(data.splitlines()))
#     print("Words =", len(data.split()))
# except FileNotFoundError:
#     print("File Not Found")
# except PermissionError:
#     print("Permission Denied")
# finally:
#     print("Program Completed")

