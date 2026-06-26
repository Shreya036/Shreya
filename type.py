# num=input("Enter number:")
# print(type(num))
# x=int(input("enter 1st number:"))
# y=int(input("enter 2nd number:"))
# z=int(input("enter 3rd number:"))
# avg=(x+y+z)/3
# print("average of 3  numbers is:",avg)
# print(type(avg))
# x="shreya"
# y="shetty"
# print(x+y)
# x=10
# del x
# print(x)
# x="shreya"
# y="shetty"
# del x
# print(y)
# print(x)
# a=10
# b=20
# c=a
# a=b
# b=c
# print("a:",a)
# print("b:",b)
# print("c:",c)
# a=(int(input("enter 1st number:")))
# b=(int(input("enter 2nd number:")))
# sum=a+b
# print("sum:",sum)   
# a=(int(input("enter 1st number:")))
# b=(int(input("enter 2nd number:")))
# sub=a-b
# print("subtraction:",sub)
# a=(int(input("enter 1st number:")))
# b=(int(input("enter 2nd number:")))
# mul=a*b
# print("multiplication:",mul)
# a=(int(input("enter 1st number:")))
# b=(int(input("enter 2nd number:")))
# div=a/b
# print("division:",div)
# a=10
# print(type(a))
# b=10.5
# print(type(b))
# c="shreya"
# print(type(c))
# d=10+5j
# print(type(d))
# x="welcome to python programming"
# print(x[-3])
# x="welcome to python programming"
# print(x[4])
# x="welcome to python programming"
# print(x[0:11:2])
# x="welcome to python programming"
# print(x[::-1])
# s='Hello World'
# print(s)
# y="hello world"
# print(y)
# z="""Hello World
# how are you?"""
# print(z)
# x="Welcome to python programming"
# print(x[1:4])
# x="py"
# y="thon"
# z=x+y
# print(z)
# x="11"*3
# print(x)
# x="py" in "python"
# print(x)
# x=len("python")
# print(x)
# x="python programming"
# print(x.upper())
# x="PYTHON PROGRAMMING"
# print(x.lower())
# x="python programming"
# print(x.title())
# x="python programming"
# print(x.capitalize())  
# x="pYtHON PRoGrAmming"
# print(x.swapcase())
# print("hyy malini".find("y"))
# print("hyy malini".index("l"))
# print("hyy malini".count("i"))
# print("hyy malini".startswith("ma"))
# print("hyy malini".endswith("ni"))
# print("hellow".replace("h","H"))
# print(("   hi  hello   ".strip()))
# print(("    hi".lstrip()))
# print(("hi  ".rstrip()))
# print("a,b,c".split(","))
# print("_".join(["hello","world"]))
# print("abc".isalpha())
# print("adf".isdigit())
# print("abc123".isalnum())
# print("aBC".islower())
# print("ABc".isupper())
# print(f"Age {25}")
# print("age {}".format(25))
# x=10
# del x
# print(x)
# for i in range(1,10,2):
#     print(i)
# for i in "python":
#         print(i)
# for i in range(1,11):
#     print(i)
# x=int(input("enter number:"))
# for i in range(1,11):
#     print(f"{x} x {i} = {x*i}")
# x=int(input("enter number:"))
# x=1
# while x<=10:
#     print(f"{x}*{x}={x*x}")
#     x=+1
# x=input("enter string:")
# ch=""
# for i in x:
#     ch=i+ch
# print(ch)
# x=input("enter string:")
# ch=""
# while x:
#     length=len(x)
#     ch=ch+x[length-1]
#     x=x[:length-1]
# print(ch)
# x=str(input("enter string:"))
# i=len(x)-1
# while i>=0:
#     print(x[i],end=" ")
#     i=i-1   
# x=int(input("enter number:"))
# if x%2==0:
#     print("even")
# else:   
#      print("odd")
# x=int(input("enter number:"))
# if x>0:
#     print("positive")
# elif x<0:
#     print("negative")
# else:    
#     print("zero")
# x=int(input("enter  1st number:"))
# y=int(input("enter 2nd number:"))
# z=int(input("enter 3rd number:"))
# if x==y and x==z:
#     print("all numbers are equal")
# elif x==y or x==z or y==z:
#     print("two numbers are equal")
# else:
#     print("all numbers are different")
# x=int(input("enter number:"))
# for i in range(1,15):
#     if i==11:
#         break
#     if i==5:
#         continue
#     if i==10:
#         pass
#     print(i)
# else:
#     print("completed successfully")
# print(ord('a'))
# print(chr(65))
# a=input("enter strung")
# for i in a:
#     if i.isalpha()==True:
#         if i=='z':
#             next_letter='a'
#         elif i=='z':
#             next_letter='A'
#         else:
#             next_letter=chr(ord(i)+1)
#         print(next_letter,end="")
#     else:
#         print(i,end="")
# year=int("enter year")
# if year%400==0:
#     print("leap year")
# elif year % 4==0 and year % 100!=0:
#     print("leap year")
# else:
#     print("not a leap yaer")
# name=input("enter string:")
# v=0
# c=0
# for i in name:
#         if i in "aeiouAEIOU":
#                 v+=1
#         elif i.isalpha():
#                 c+=1
# print("vowels=",v)
# print("consonant=",c)
# n=int(input("enter a number:"))
# if str(n)==str(n)[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
# n=int(input("enter a number:"))
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print("Fact=",factorial)
# count=10
# a=0
# b=1
# for i in "count":
#     print(a)
#     a,b=b,a+b
# n=4
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     print(" ".join([str(i)]*i))
# row=3
# for i in range(1,row+1):
#     print(" "*(row-i),end=" ")
#     print(" *"*i)
# n=3
# num=1
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(num,end=" ")
#         num=num+1            
#     print()
# rows=3
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# a=[1,2,3]
# print(a)
# a=[1,2,3]
# print(a[1])
# print(a[-1])
# print(a[0:2])
# print(len(a))
# a.append(4)
# print(a)
# a.insert(1,10)
# print(a)
# a.extend([5,6])
# print(a)
# print(a+[7,8])
# a.remove(2)
# print(a)
# a.pop()
# print(a)
# a.pop(1)
# print(a)
# a.clear()
# print(a)
# a=[1,9,2,8,3,7,4,5,6]
# a.index(3)
# print(a)
# a.count(2)
# print(a)
# print(2 in a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.reverse()
# print(a)
# sorted(a)
# b=a.copy()
# print(b)
# print(list("abc"))
# print(a*2)
# squares=[x**2 for x in range(10)]
# print(squares)
# evens=[x for x in range(10)if x %2==0]
# print(evens)
# fruits=["apple","banana","cherry"]
# upper_fruits=[fruit.upper()for fruit in fruits]
# print(upper_fruits)
# rags=["Even"if x % 2==0 else "Odd" for x in range(5)]
# print(rags)
# t=(1,2,3)
# print(t)
# t=1,2,3
# print(t)
# print(t[1])
# print(t[-1])
# print(t[0:2])
# print(len(t))
# print((1,2)+(3,4))
# print((1,2)*2)
# print(2 in (1,2,3))
# t=(1,2,3,4,5,6,7,8,9)
# print(t)
# j=(list((t)))
# j.insert(5,15)
# print(j)
# s=(tuple((j)))
# print(s)
# t=1,2,3
# print(t)
# a,b,c=t
# print(a+b+c)
# t=((1,2),"banana",[2,5],)
# print(t[2])
# print(t[2][1])
# t[2][1]=10
# print(t)
# a
# num=frozenset([1,2,3,4])
# print(num)
# n={1,2,3,4,4,4,}
# print(len(n))
# n=set()
# print(n)
# n.add(10)
# print(n)
# n.update([11,23])
# print(n)
# n.pop()
# print(n)
# n.remove(11)
# print(n)
# n.discard(2)
# print(n)
# n.clear()
# print(n)
# A={1,2,3,3,4,5,6,}
# B={1,9,10,3,4,6,7}
# print(A.union(B))
# print(A.intersection(B))
# print(A.difference(B))
# print(A.symmetric_difference(B))
# a={"shreya","swathi"}
# b={19,2,24,3,8}
# A.update(a,b)
# print(A)
# B.intersection_update({"hai",1,4,5,6})
# print(B)
# A.difference_update({32,6,5})
# print(A)
# B.symmetric_difference_update({"hyy",1,2,3,4,5})
# print(B)
# a={1,2,3,4}
# b={4,5,6,}
# print(a.issubset(a))
# print(a.issuperset(b))
# s={1,2,3,4,5}
# b=s.copy()
# print(b)
# print(sorted(s))
# print(max(s))
# print(min(s))
# print(sum(s))
# d={"name":"anu","age":24}
# print(d["name"])
# print(d["age"])
# d={"a":1,"b":2,"c":3,"d":4}
# print(d["a"])
# print(d.get("a"))
# d.update({"b":5})
# print(d)
# d.setdefault("d",4)
# print(d)
# d["c"]=3
# d.pop("a")
# print(d)
# d.popitem()
# print(d)
# print(d.values())
# print(d.keys())
# print(d.items())
# d={"a":1,"b":2,"c":32,"d":"apple"}
# print(d.copy())
# print(dict([(1,'a')]))
# print("d" in d)
# print("a" not in d)
# for k in d:
#     print(k)
# for v in d.values():
#         print(v)
# for k,v in d.items():
#       print(k,v)
# d["city"]="kochi"
# print(d)
# x=("aple","shreya",1,2)
# y=("aple","shreya",1,2)
# c=x
# print(x==y)
# print(x is y)
# print(x is c)
# print(id(x))
# print(id(y))
# print(id(c))
# point=(10,20)
# match point:
#     case(0,0):
#         print("Origin")
#     case(0,y):
#         print(f"On y-axis at {y}")
#     case(x,0):
#         print(f"On x-axis at {x}")
#     case(x,y):
#         print(f"point at {x},{y}")
# x=10
# result="even"if x%2==0 else"odd"
# print(result)
# a=[5,2,8,7,10]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# n=int(input("emter a number:"))
# digits=len(str(n))
# s=0
# for i in str(n):
#     s+=int(i)**digis
# if s==n:
#     print("Armstrong number")
# else:
#     print("not armstrong number")
# n=int(input("enter a number:"))
# r=0
# while n:
#     r=r*10+n%10
#     n//=10
# print(r)


# import random
# word =random.choice(["apple", "mango", "grapes"])
# display = ["_"] * len(word)
# while "_" in display:
#     letter = input("Enter a letter: ")
#     for i in range(len(word)):
#         if word[i] == letter:
#             display[i] = letter
#     print(" ".join(display))
# print("You guessed the word:", word)




# python_students = {"Arun", "Megha", "Rahul", "Sneha"} 
# analytics_students = {"Sneha", "Rahul", "Aman", "Diya"} 
# print(python_students.intersection(analytics_students))
# print(python_students.difference(analytics_students))
# print(analytics_students.difference(python_students))
# print(python_students.union(analytics_students))
# print(python_students.symmetric_difference(analytics_students))
# customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
# customer2 = {"Appe", "Vivo", "Oppo", "Samsung"} 
# print(customer1.intersection(customer2))
# print(customer1.union(customer2))
# print(customer1.difference(customer2))
# print(customer1.symmetric_difference(customer2))
# design_team = {"Figma", "Photoshop", "Canva", "Illustrator"}
# marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"} 
# print(design_team.intersection(marketing_team))
# print(design_team.difference((marketing_team)))
# print(design_team.union(marketing_team))
# print(design_team.symmetric_difference(marketing_team))
# cricket_fans = {"Ajay", "Kiran", "Rohit", "Nisha"}
# football_fans = {"Nisha", "Rahul", "Ajay", "David"}
# print(cricket_fans.intersection(football_fans))
# print(cricket_fans.difference(football_fans))
# print(football_fans.difference(football_fans))
# print(cricket_fans.union(football_fans))
# emp1 = {"Python", "Java", "SQL", "C"}
# emp2 = {"Python", "JavaScript", "SQL", "Go"}
# print(emp1.union(emp2))
# print(emp1.difference(emp2))
# print(emp1.intersection(emp2))
# print(emp1.symmetric_difference(emp2))
# restaurant1 = {"Burger", "Pizza", "Fries", "Pasta"}
# restaurant2 = {"Pizza", "Sandwich", "Pasta", "Momos"}
# print(restaurant1.intersection(restaurant2))
# print(restaurant1.difference(restaurant2))
# print(restaurant2.difference(restaurant1))
# print(restaurant1.union(restaurant2))
# print(restaurant1.symmetric_difference(restaurant2))
# d={"basic":35000,"bonus":5000,"tax":2000}
# d["total"]=d["basic"]+d["bonus"]
# print(d)
# d["tax"]=d["total"]-d["tax"]
# print(d)
# d["finalsalary"]=(d["tax"]*12)
# print(d)
# d["yearly"]=d["finalsalary"]//12
# # print(d)
# d={"mobileprice":45000,"discount":5000,"gst":2000}
# d["discountprice"]=d["mobileprice"]-d["discount"]
# d["add"]=d["discountprice"]+d["gst"]
# d["final"]=d["add"]/2
# d["amouunt"]=d["final"]%3
# print(d)
# d={"python":85,"sql":78,"mark":90}
# d["total"]=d["python"]+d["sql"]+d["mark"]
# d["avg"]=d["total"]/3
# d["greater"]=d["python"]>d["sql"]
# d["equal"]=d["mark"]=d["python"]
# print(d)
# s= { "name": "Rahul", "course": "Data Science", "marks": 88, "city": "Bangalore"}
# print(s["name"])
# print(s["course"])
# s.update({"marks":95})
# print(s)
# s["email"]="rahul@gmail.com"
# print(s)
# del s["city"]
# print(s)
# print(s)
# emp={"id":101,"name":"Anjali","department":"HR","salary":45000}
# print("salary",emp["salary"])
# emp["salary"]+=5000
# print("upsalary:",emp["salary"])
# emp["location"]="kochi"
# print(emp)
# emp.pop("department")
# print(emp)
# print("keys",emp.keys())
# mob={"brand":"nokia","model":"524","price":75000,"storage":"256GB"}
# print(mob["model"])
# mob.update({"price":70000})
# print(mob)
# mob["color"]="black"
# mob.pop("storage")
# print(mob)
# movie = { "title": "Leo", "hero": "Vijay", "rating": 8.5, "language": "Tamil"}
# print(movie["title"])
# movie.update({"rating":9.1})

# Company_name = "TechNova Solutions"
# employee_name = "Arjun Menon"
# employee_id = "TNX2026"
# department = "Data Analytics"
# skills = ["Python", "SQL", "Excel", "Power BI", "Tableau"]
# monthly_salary = 45000
# bonus = 5000
# working_days = 26
# absent_days = 2
# project_details = (
# "Customer Churn Analysis",
# "Completed",
# "Power BI Dashboard"
# )
# email = "arjun.menon@technova.com"
# # Print the company name in:uppercase, lowercase, title case
# print(company_name.upper())
# print(company_name.lower())
# print(company_name.title())
# print(len(employee_name))
# print(department.replace("Data Analytics","Data Science")
# print("first name:",employee_name[:5])
# print("last name:",employee_name[-5:])
# print(employee_id[:5])
# print("Nova" in company_name)
# print("Employee "+employee_name+ " Works in " +department+ " department.")
# print(email.split("@")[0])
# list
# Print: first skill, last skill
# print("first skill:",skills[0])
# print("last skill:",skills[-1])
# # Add "Machine Learning" to skills list.
# skills.append("Machine Learning")
# print(skills)
# Insert "Statistics" at 2nd posrition.
# skills.insert(2,"Statistics")
# print(skills)
# # 12. Remove "Excel" from list.
# skills.remove("Excel")
# print(skills)
# # Sort skills alphabetically.
# skills.sort()
# print(skills)
# # Reverse the skills list.
# skills.reverse()
# print(skills)
# # 15. Find total number of skills.
# print(len(skills))
# # 16. Create another list:
# # tools = ["Git", "Jupyter Notebook"]
# # Merge it with skills list.
# tools = ["Git", "Jupyter Notebook"]
# skills.extend(tools)
# print(skills)
# # Check whether "SQL" exists in skills list.
# print("SQL" in skills)
# # Print skills from index 1 to 4 using slicing.
# print(skills[0:4])
# # tuple
# # Print all project details.
# print(project_details)
# # Print project status only.
# print(project_details[1])
# # Find total number of elements in project_details tuple.
# print(len(project_details))
# # Check whether "Completed" exists in tuple.
# print("Completed" in project_details)
# # Create another tuple:
# # project_manager = ("Rahul",)
# # Combine both tuples.
# project_manager = ("Rahul",)
# print(project_details + project_manager)
# #operator
# # 24.Calculate:
# # total_salary = monthly_salary + bonus
# total_salary = monthly_salary + bonus
# print(total_salary)
# # Calculate salary per working day.
# print(total_salary//working_days)
# # Calculate salary deduction for absent days.
# # Formula:
# # (monthly_salary / working_days) * absent_days
# print((monthly_salary//working_days)*absent_days)
# # Use assignment operator: Increase salary by 3000.
# print(monthly_salary+3000)
# # Check: monthly_salary > bonus
# print(monthly_salary > bonus)
# # Check identity operator:
# # skills is tools
# print(skills is tools)
# # Check logical operator:
# # monthly_salary > 40000 and bonus > 3000
# print(monthly_salary > 40000 and bonus > 3000)




# def greet():
    # print("welcome to python")
# greet()
# def find_square(num):
#     reult=num*num
#     return result
# square=find_square(3)
# print(square)
# sqrt_root=math.sqrt(4)
# print("square root of 4 is"square root)
# print(square_root)
# def is_armstrong(a):
#     n=str(a)
#     c=len(n)
#     total=0
#     for i in n:
#         total+=int(i)**c
#     return total==a
# print(is_armstrong(153))
# def show(a,b):
#     print(a,b)
# show(10,20)
# def show(a,b):
#     print(a,b)
# show(a=10,b=20)


# def greet(name="student"):
#     print("Hellow",name)
# greet()
# def display(**details):
#     print(details)
# display(name="anu",age=24,city="kochi")
# def greet(name,greeting="hello"):
#     print(f"{greeting},{name}!")
# greet("Arjun")
# greet("maya","hi")
# greet(name="sara",greeting="hey")
# def total_cost(price,*,tax=0.18,tip=0):
#     return price+(price*tax)+tip
# print(total_cost(100,tip=10))
# def divide(a,b,/):
#     return a/b
# # print(divide(10,2))
# def multiply_all(*nums):
#     result=1
#     for n in nums:
#         result*=n
#     return result
# print(multiply_all(2,3,4))
# print(multiply_all())
# def built_sentences(**words):
    # return " ".join(words.values())
# print(built_sentences(a="python",b="is",c="fun"))
# def order_pizza(size, *toppings, crust="thin", **extras):
#     return {
#         "size": size,
#         "toppings": toppings,
#         "crust": crust,
#         "extras": extras
#     }
# print(order_pizza(
#     "Large",
#     "mushrooms",
#     "onions",
#     cheese="extra",
#     delivery=True
# ))



# sum=lambda a,b:a+b
# print(sum(5,4))
# check = lambda n: "Even" if n % 2 == 0 else "Odd"
# print(check(10))
# check=lambda x: "positive" if x>0 else"negetive" if x<0 else "zero"
# print(check(10))
# print(check(-1))
# print(check(0))

# a=[1,2,3,4,5]
# double=list(map(lambda x:x*2,a))
# print(double)

# a=[1,2,3,4,5,6,7,8,9]
# square=list(map(lambda x:x**2,a))
# print(square)

# even=list(filter(lambda x:x%2==0,a))
# print(even)

# odd=list(filter(lambda x:x%2==1,a))
# print(odd)

# multiple=list(filter(lambda x:x%3==0,a))
# print(multiple)

# from functools import reduce
# sum= reduce(lambda acc,y:acc+y,a)
# print(sum)
# sum=reduce(lambda acc,y:acc+y,a)
# print("natural num",sum)
# even=list(filter (lambda x:x%2==0,a))
# even=reduce(lambda acc,y:acc+y,even)
# print("even",even)
# odd=list(filter (lambda x:x%2==1,a))
# odd=reduce(lambda acc,y:acc+y,odd)
# print("odd",odd)
# import random
# number=str(random.choice([10,11,43,56.76,15]))
# display = ["_"] * len(number)
# while "_" in display:
#     digit = input("Enter a digit: ")
#     for i in range(len(number)):
#         if number[i] == digit:
#             display[i] = digit
#     print(" ".join(display))
# print("You guessed the number:", number)
# func=[lambda arg=x:arg*10 for x in range(1,5)]
# for i in func:
#     print(i())


#                                                                   FILE HANDLING
#                                                                 #----------------#


# file=open("sample.txt","r")
# print(file.read())
# file.close()


# file=open("sample.txt","w")
# file.write("hello python")
# file.close()

# file=open("sample.txt","a")
# file.write("learning file handling")
# file.close()

# import os
# os.remove("sample.txt")
# print("file deleted succesfully")

# file=open("sample.txt","x")
# file.close()

# file=open("sample.txt","r")
# print(file.readlines())
# file.close()

# file=open("sample.txt","r")
# print(file.readline())
# file.close()


# file=open("sample.txt","w")
# file.writelines(["hello python"])
# file.close()


# with open("sample.txt","r")as f:
#     print(f.read())


# file=open("sample.txt","r")
# sample=file.read()
# count=0
# result=""
# for i in sample:
#     if i.lower() in "aeiou":
#         count+=1
#         result+=i.upper()
#     else:
#         result+=i
# print("number of vowels:",count)
# print(result)
# file.close()

# vowels="aeiouAEIOU"
# vowels_count=0
# new_content=""
# with open("sample.txt","r")as f:
#     content=f.read()
#     for char in content:
#         if char in vowels:
#             vowels_count+=1
#     for char in content:
#         if char in "aeiou":
#             new_content+=char.upper()
#         else:
#             new_content+=char
# with open("sample.txt","w")as f:
#           f.write(new_content)
# print(f"Vowels found:{vowels_count}")
# print("Vowels changed to uppercase")


#                                                           file&exception

# file = open("sample.txt","w")
# file.close()
# print("File created")

# file = open("sample.txt","w")
# file.write("Name: Shreya,Age: 20")
# file.close()

# file = open("sample.txt","r")
# print(file.read())
# file.close()


# file = open("sample.txt","a")
# file.write("New content added")
# file.close()


# file = open("sample.txt","r")
# data = file.read()
# print("Characters:",len(data))
# file.close()

# file = open("sample.txt","r")
# data = file.read()
# words = data.split()
# print("Words:",len(words))
# file.close()


# file = open("sample.txt","r")
# lines = file.readlines()
# print("Lines:",len(lines))
# file.close()

# file = open("sample.txt","r")
# for i in range(5):
#     print(file.readline())
# file.close()


# f1 = open("sample.txt","r")
# f2 = open("copy.txt","w")
# f2.write(f1.read())
# f1.close()
# f2.close()


# f1=open("sample.txt","r")
# f2=open("sample.txt","r")
# f3=open("merge.txt","w")
# f3.write(f1.read())
# f3.write(f2.read())
# f1.close()
# f2.close()
# f3.close()


# file=open("sample.txt","r")
# data=file.read()
# count=0
# for ch in data:
#     if ch.lower() in "aeiou":
#         count+=1
# print(count)
# file.close()


# file=open("sample.txt","r")
# data=file.read()
# data=data.replace("old","new")
# file=open("sample.txt","w")
# file.write(data)
# file.close()


# file=open("sample.txt","r")
# data=file.read()
# data=data.replace(" ","")
# file=open("sample.txt","w")
# file.write(data)
# file.close()



# f1=open("sample.txt","r")
# f2=open("upper.txt","w")
# f2.write(f1.read().upper())
# f1.close()
# f2.close()


# file=open("sample.txt","r")
# words=file.read().split()
# for word in set(words):
#     print(word)
# file.close()




                                                           #####Exception handling#######



# try:
#     a=10/0
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# try:
#     n=int(input("Enter number:"))
# except ValueError:
#     print("Invalid input")


# try:
#     file=open("abc.txt","r")
# except FileNotFoundError:
#     print("File not found")

# try:
#     a=[1,2,3]
#     print(a[5])
# except IndexError:
#     print("Index error")


# try:
#     print("5"+5)
# except TypeError:
#     print("Type error")



# try:
#     x=int(input())
#     print(10/x)
# except ValueError:
#     print("Value error")
# except ZeroDivisionError:
#     print("Zero division")


# try:
#     file=open("sample.txt")
#     print(file.read())
# finally:
#     file.close()
#     print("File closed")


# try:
#     a=10/2
# except:
#     print("Error")
# else:
#     print("No error")



# try:
#     username=input("Username:")
#     password=input("Password:")
#     if username=="admin" and password=="1234":
#         print("Login successful")
#     else:
#         raise Exception("Invalid login")
# except Exception as e:
#     print(e)



# balance = 5000
# pin = 1234
# try:
#     entered_pin = int(input("Enter PIN: "))
#     if entered_pin != pin:
#         raise Exception("Invalid PIN")
#     amount = int(input("Enter withdrawal amount: "))
#     if amount > balance:
#         raise Exception("Insufficient balance")
#     elif amount <= 0:
#         raise Exception("Invalid amount")
#     balance -= amount
#     print("Withdrawal successful")
#     print("Remaining balance:", balance)
# except Exception as e:
#     print(e)


# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     op = input("Enter operation (+,-,*,/): ")
#     if op == '+':
#         print(a+b)
#     elif op == '-':
#         print(a-b)
#     elif op == '*':
#         print(a*b)
#     elif op == '/':
#         print(a/b)
#     else:
#         print("Invalid operator")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Enter numbers only")



# try:
#     age = int(input("Enter age: "))
#     if age < 0:
#         raise Exception("Invalid age")
#     print("Valid age")
# except Exception as e:
#     print(e)



# while True:
#     try:
#         n = int(input("Enter a number: "))
#         print("Valid input:", n)
#         break
#     except ValueError:
#         print("Invalid input, try again")

# try:
#     file = open("sample.txt","r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
# #     print("File not found")


# class BalanceError(Exception):
#     pass
# try:
#     balance = 1000
#     withdraw = 2000
#     if withdraw > balance:
#         raise BalanceError("Insufficient balance")
# except BalanceError as e:
#     print(e)


# class PasswordError(Exception):
#     pass
# try:
#     password = input("Enter password: ")
#     if password != "python123":
#         raise PasswordError("Invalid password")
#     print("Login successful")
# except PasswordError as e:
#     print(e)



# class AgeError(Exception):
#     pass
# try:
#     age = int(input("Enter age: "))
#     if age < 18:
#         raise AgeError("Not eligible for voting")
#     print("Eligible")
# except AgeError as e:
#     print(e)

# class MarksError(Exception):
#     pass
# try:
#     marks = int(input("Enter marks: "))
#     if marks < 0:
#         raise MarksError("Negative marks not allowed")
#     print("Marks:", marks)
# except MarksError as e:
#     print(e)

    
# class StockError(Exception):
#     pass
# try:
#     stock = 0
#     if stock == 0:
#         raise StockError("Product out of stock")
# except StockError as e:
#     print(e)


# file = open("sample.txt","w")
# file.write("")
# file.close()
# print("All contents deleted")






# # class aaand obj

# class arithmetic:
#     def arith(A,a,b):
#         b=(int(input("enter a number")))
#         b=(int(input("enter a number")))
#         print("addition",a+b)
#         print("substraction",a-b)
#         print("mutiplication",a*b)
#         print("div",a/b)
# s=arithmetic() 
# s.arith(0,0)          

# class Student:
#     a="biriyani"
#     def Food(A):
#         print(A.a)
# x=Student()
# x.Food

############################################encapsulation###############################

# class Demo:
#     def __init__(A):
#         A.__x=10
#     def show(A):
#         print(A.__x)
# d=Demo()
# d.show()

# class Demo:
#     def __init__(A):
#         A.public = 10
#         A._protected = 20
#         A.__private = 30
#     def show(A):
#         print(A.public, A._protected, A.__private)
# obj = Demo()
# obj.show()
# print(obj.public)       
# print(obj._protected)   



# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     def strat(self):
#         pass
# class Car(Vehicle):
#     def start(self):
#         print("Car is starting...")
# c=Car()
# c.start()



              ###############ooooooop###################
# class Student:
#     def __init__(A, name, age, course):
#         A.name = name
#         A.age = age
#         A.course = course
#     def display(A):
#         print("Name:", A.name)
#         print("Age:", A.age)
#         print("Course:", A.course)
#         print()
# s1 = Student("Swathi", 20, "Python")
# s2 = Student("likitha", 21, "Data analytics")
# s3 = Student("shreya", 19, "AI")
# s1.display()
# s2.display()
# s3.display()


# class Mobile:
#     def __init__(A, brand, model, price):
#         A.brand = brand
#         A.model = model
#         A.price = price
#     def display(A):
#         print(A.brand, A.model, A.price)
# m1 = Mobile("Samsung", "S24", 80000)
# m2 = Mobile("Apple", "iPhone", 90000)
# m1.display()
# m2.display()



# class Employee:
#     def __init__(A, emp_id, name, salary):
#         A.emp_id = emp_id
#         A.name = name
#         A.salary = salary
#     def display(A):
#         print(A.emp_id, A.name, A.salary)
# e1 = Employee(1,"Arun",30000)
# e2 = Employee(2,"Anu",40000)
# e3=Employee(3,"rahul",5000)
# e4=Employee(4,"mok",5647)
# e5=Employee(5,"sahal",5896)
# e1.display()
# e2.display()
# e3.display()
# e4.display()
# e5.display()


# class Book:
#     def __init__(A, title, author, price):
#         A.title = title
#         A.author = author
#         A.price = price
#     def display(A):
#         print(A.title,A.author,A.price)
# b1 = Book("Python","Guido",500)
# b2 = Book("Java","James",600)
# b1.display()
# b2.display()


# class BankAccount:
#     def __init__(A, holder, number, balance):
#         A.holder = holder
#         A.number = number
#         A.balance = balance

#     def display(A):
#         print(A.holder)
#         print(A.number)
#         print(A.balance)
# a1 = BankAccount("Shreya",12345,5000)
# a1.display()




# class Student:
#     name = "Swathi"
#     age = 20
#     course = "Python"
# s1 = Student()
# print("Name:", s1.name)
# print("Age:", s1.age)
# print("Course:", s1.course)


# class Car:
#     def __init__(A,brand,model,price):
#         A.brand=brand
#         A.model=model
#         A.price=price
#     def display(A):
#         print(A.brand,A.model,A.price)
# c1=Car("alto","a6",6000000)
# c1.display()




# class Hospital:
#     def __init__(A,patient,age,disease):
#         A.patient=patient
#         A.age=age
#         A.disease=disease
#     def display(A):
#         print(A.patient,A.age,A.disease)
# h1=Hospital("swathi","21","loosemotion")
# h1.display()




# class Movie:
#     def __init__(A,moviename,number,price):
#         A.moviename=moviename
#         A.number=number
#         A.price=price
#     def display(A):
#         print(A.moviename,A.number,A.price)
# c1=Movie("happy","45",600)
# c1.display()


# class Calculator:
#     def add(A,a,b):
#         print("Addition:",a+b)
#     def sub(A,a,b):
#         print("Subtraction:",a-b)
#     def mul(A,a,b):
#         print("Multiplication:",a*b)
#     def div(A,a,b):
#         print("Division:",a/b)
# c = Calculator()
# c.add(10,5)
# c.sub(15,5)
# c.mul(167,5)
# c.div(15,5)


# class ATM:
#     def deposit(A,amount):
#         A.balance += amount
#     def withdraw(A,amount):
#         A.balance -= amount
#     def check_balance(A):
#         print("Balance:",A.balance)
# a = ATM()
# a.balance = 5000
# a.deposit(1000)
# a.withdraw(500)
# a.check_balance()

# class ShoppingCart:
#     def addproduct(A,item):
#      A.cart.append(item)
#     def removeproduct(A,item):
#         A.cart.remove(item)
#     def showcart(A):
#         print(A.cart)
# s = ShoppingCart()
# s.cart = []
# s.addproduct("Mobile")
# s.addproduct("Laptop")
# s.removeproduct("Mobile")
# s.showcart()


# class ShoppingCart:
#     def __init__(A):
#         A.cart = []
#     def add_product(A, product):
#         A.cart.append(product)
#         print(f"{product} added to cart")
#     def remove_product(A, product):
#         if product in A.cart:
#             A.cart.remove(product)
#             print(f"{product} removed from cart")
#         else:
#             print(f"{product} not found in cart")
#     def show_cart(A):
#         if A.cart:
#             print("Shopping Cart:")
#             for item in A.cart:
#                 print("-", item)
#         else:
#             print("Cart is empty")
# cart = ShoppingCart()
# cart.add_product("Laptop")
# cart.add_product("Mouse")
# cart.show_cart()
# cart.remove_product("Mouse")
# cart.show_cart()


# INHERITANCE############
# class vehicle:
#     def display(A):
#         print("this is a vehicle")
# class Car(vehicle):
#     def display(A):
#         print("this is a car")
# c=Car()
# c.display()


# class Employee:
#     def __init__(A, name, salary):
#         A.name = name
#         A.salary = salary
# class Manager(Employee):
#     def display(A):
#         print("Manager:", A.name, A.salary)
# class Developer(Employee):
#     def display(A):
#         print("Developer:", A.name, A.salary)
# class Tester(Employee):
#     def display(A):
#         print("Tester:", A.name, A.salary)
# m = Manager("Anu", 50000)
# d = Developer("Rahul", 40000)
# t = Tester("Asha", 30000)
# m.display()
# d.display()
# t.display()


# class Person:
#     def display(B):
#         print("This is a person")
# class Teacher(Person):
#     def display(B):
#         print("Role: Teacher")
# class Student(Person):
#     def display(B):
#         print("Role: Student")
# t = Teacher()
# s = Student()
# t.display()
# s.display()

# class Animal:
#     def eat(B):
#         print("Animal eats")
# class Mammal(Animal):
#     def walk(B):
#         print("Mammal walks")
# class Dog(Mammal):
#     def bark(B):
#         print("Dog barks")
# d = Dog()
# d.eat()
# d.walk()
# d.bark()


# class Person:
#     def hy_person(self,name,age):
#         self.name=name
#         self.age=age
# class Student(Person):
#     def hy_student(self):
#         print("Student details")
# class GraduateStudent(Student):
#     def hy_graduate(self):
#         print("Graduate student details")
# g = GraduateStudent()
# g.hy_person()
# g.hy_student()
# g.hy_graduate()


# class Parent:
#     def __init__(self,tell):
#         self.tell=tell
#     def display(self):
#         print(self.tell)
# class Child(Parent):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def display(self):
#       print(self.age)
#       super().display()
# hat=Parent(tell="hellow")
# obj=Child(name="shreya",age=20)
# obj.display()
# hat.display()

# class Animal:
#     def speak(self):
#         return"some generic sound"
# class Dog(Animal):
#     def speak(self):
#         return"Woof!"
# class Cat(Animal):
#     def spaek(self):
#         return "Meow!"
# animals=[Dog(),Cat(),Animal()]
# for i in animals:
#     print(i.speak())



class ATM:
    def __init__(self,pwd,balance):
        self.pwd=pwd
        self.balance=balance
    def withdraw(self):
        if int(input("password"))==self.pwd:
            amount=int(input("Amount"))
            self.balance-=amount
            print("balance",self.balance)
        else:
            print("wrong")
a=ATM(1234,10000)
a.withdraw()





