# class bankaccount:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposite(self):
#         if self.balance < 0:
#             print("Insufficient balance")
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#     def check_balance(self):
#         print(f"Account Number: {self.account_number}")
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance: {self.balance}")
# c=bankaccount("123456789", "John Doe", 1000)
# c.deposite()
# c.withdraw(1000)
# c.check_balance()       


# python=int(input("enter a mark"))
# maths=int (input("enter  mark"))
# c=int(input("enter  mark"))
# java=int(input("enter  mark"))
# python=int(input("enter  mark"))
# sum=python+maths+c+java+python
# if sum>=75:
#     print("Distinction")
# else:
#     if sum<=40:
#         print("pass")
#     else:
#         if sum<40:
#             print("fail")

# class employee:
#     def __init__(self, employee_name,department,salary):
#         self.employee_name = employee_name
#         self.department = department
#         self.salary = salary
#         def display(self):
#             if self.salary>70000:
#                 print("seniour employee")
#             else:
                # if salary 