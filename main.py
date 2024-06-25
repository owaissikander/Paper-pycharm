# a = 12
# print(a)
# b = 3 + a
# print(b)
# c = 15
# print(b+c)
#

# firstName = "Owais"
# lastName = "Khan"
# print(f'this is my {firstName} and this is my last name {lastName}')
# print('This is my first Name '+firstName+' And this is my last name '+lastName)
# print('this  is my first name', firstName, 'this is last name', lastName)


# name,age,std_class ='owais', "22", "BSCS"
# print(name,age, std_class)
# print('This is my name',name,'this is my age',age ,'this is my class',std_class)
#
# print(name + age + std_class)

#using if else statement assing grade

# mark = int(input('Enter your makes'))
# if 90 <= mark:
#     print('A')
# elif 80 <= mark:
#     print('B')
# elif 70 <= mark:
#     print('C')
# elif 60 <= mark:
#     print('D')
# else:
#     print('Failed')
#     print("\n")


# own practice

# mark = 85
# if 90 <= mark:
#     print('A')
# elif 80 <= mark:
#     print('B')
# elif 70 <= mark:
#     print('C')
# elif 60 <= mark:
#     print('D')
# else:
#     print('Failed')


# student = {
#     "name": "owais",
#     "father_Name": 'Sikander',
#     "education": 'BSCS',
#     "age": 22
#
# }
#
# print(student["father_Name"], student['name'])
# print(student["education"], student["age"])
#

my_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
my_list2 = [11, 12, 13, 14]


print(my_list[5],my_list[5],my_list[5])
print('this is length of my list', len(my_list))

#for find length of list
print(len(my_list))
#
# #for invrement
# print(my_list[-1],my_list[-1],my_list[-0])

# #for push new value
# my_list[0]=10
# print(my_list)
# my_list[5]="owais"
# print(my_list)


#
# #for accesing the list
# my_list[0:4]
# print(my_list[0:4])
#
# #first_Methods
# list = my_list+ my_list2
# print(list)
# #second_Methods
# print(my_list,my_list2)

#apennd function is use to add new value in the list at end of list
# my_list2.append(15)
# print(my_list2)
# #extend function is use to add new value in the list at any position
# my_list2.extend([16,17,18,19])
# print(my_list2)
my_list2.insert(1,100)
print(my_list2)
# #take item name and does it remove
my_list2.remove(100)
print(my_list2)
# #take index number and delete on that index number
my_list2.pop(2)
# print(my_list2)
# my_list2.clear()
# print(my_list2)
# del my_list2
print(my_list2)
# copy fu is use to copy the list
# my_list2 = my_list.copy()
# print(my_list2)

# # #copy fu is use to copy the list
# my_list14=[81,82,83,84,85]
# my_list14=my_list2.copy()
# print(my_list14)
#
# fruites =('mango','apple','banana','orange')
# print(fruites)
# print(len(fruites))
# print(type(fruites))
# print(fruites[0])

#
# sets ={9,8,7,6,5}
# print(sets)
# print(type(sets))
# print(len(sets))
# print(sets[0])# not right function
# marks = int(input('enter your marks'))
# if marks > 0 and marks < 100:
#     if marks >= 90:
#         print('A')
#     elif marks >= 80:
#         print('B')
# elif marks >= 70:
#     print('C')
# elif marks >= 60:
#     print('D')
#
# else:
#     print('Your number is not valid try again')
#

# own practice
# marks = int(input('Enter your makes'))
# if(marks>0 and marks<100):
#     if marks <90:
#         print('A')
#     elif(marks<80):
#         print('B')
#     elif(marks<70):
#         print('C')
#     elif(marks<60):
#         print("D")
#     else:
#         print('Marks are not valid')


# userID ='owais'
# userPassword = 123
# ID_name=input('Enter your ID name')
# password =int(input('Enter your password'))
# if userID==ID_name and userPassword==password:
#     print('Login')
# else:
#     print('Login failed')

# eligible for CNIC
# age = int(input('Enter your age'))
# print('\n')
# if age >= 18:
#     print('Eligible')
# else:
#     print('Not_eligble')
# print('\n')
#
# trans = input('how to get school')
# time = input('how many time it will be taken')
# print(f'it take {trans} and it take {time} minutes')


# 2-There are different rules in the United Kingdom for
# what farmers at certain ages can drive. Ask the user to
# input their age and then output the relevant information below:
# Children under 13 cannot drive any tractors.A trained and supervised
# 13 to 15 year old can drive a low-powered tractor on private flat grass.16 year
# olds with a provisional category F licence can drive tractors less than 2.45 metres
# wide/Young adults from 17 to 20 with the correct licence and training can drive tracked
# vehicles that weigh less than 3,500kg. Adults over 21 years old, with the correct licenc
# e and training, can drive all types of tractor.
# age =int(input("enter your age so i can decide you do a drive"))
# if age<13:
#     print('Children under 13 cannot drive any tractors')
# elif(age>=13 and age <=15):
#     print('A trained and supervised 13 to 15 year old can drive a low-powered tractor on private flat grass')
# elif(age<=16):
#     print('16 year olds with a provisional category F licence can drive tractors less than 2.45 metres')
# elif(age>=17 and age<=20):
#     print('wide/Young adults from 17 to 20 with the correct licence and training can drive tracked vehicles that weigh less than 3,500kg.')
# else:
#     print('Adults over 21 years old, with the correct licene and training, can drive all types of tractor.')
#
# planets =['mars','jupiter','sun']
# userPlanet=input('choose a planet')
# if userPlanet in planets:
#     print('"Sorry, you lose! The correct answer was one of the secret planets."')
# else:
#     print("Congratulations, you guessed correctly! It's not one of the secret planets.")
#

# #
# catergory = 'planet'
# user_guess = input(f'guess a {catergory}')
# planets = ['mars', 'jupiter', 'sun']
# if user_guess == planets:
#     print(f'Sorry, you lose! The correct {catergory} was {planets}')
# else:
#     print(f'Congratulations, you guessed correctly! Its not the secret {catergory}')


# catetgory ="planet"
# user_guss=input(f'select a {catetgory}')
# planets=['mars','jupiter','sun']
# if user_guss==planets:
#     print(f'Sorry, you lose! The correct {catetgory} was {planets}')
# else:
#     print(f'Congratulations, you guessed correctly! Its not the secret {catetgory} ')


# user_language = input('select on 1 to 4')
# if user_language.isdigit():
#     numbers = int(user_language)
#     if numbers == 1:
#         print('Uno')
#     elif numbers == 2:
#          print('Dos')
#     elif numbers == 3:
#          print('tres')
#     elif numbers == 4:
#          print('cuatro')
#     else:
#          print("Invalid input. Please enter a valid number.")
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num*i)

#
# colors =['red','blue','green','purple']
# for i in colors:
#     print(i)
# numbers = int(input('Enter your number whose you want a table'))
# for i in range(1, 11):
#     print(numbers, 'x', i, '=', numbers * i)
# fruites = ['Cherry', 'Banana', 'Apple', 'Mango']
# for x in fruites:
#     print(x)
#     if x == 'apple':
#         break
# for x in range(0,6):
#   print(x)

# for x in range(12, 2, -2):
#   print(x)
#
# for i in range(1,6):
#   for j in range(1,i+1):
#     print('*',end='')
#   print('\n')

# for i in range(1,6):
#   print(i,end='')
#   for j in range(1,i+1):
#     print('j',end='')
#   print('\n')
#

# #
# for i in range(6, 0,-1):
#     for j in range(1, i + 1):
#         print('*', end="")
#     print('\n')


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print('*', end="")
#     print('\n')
# number =int(input('Enter number'))
# array = ['65','66','67','68',]
# for i in array:
#
#     print(i)
# for i in range(1,6):
#     for j in range(6,1,-1):
#         print(i*j,end='')
#     print("\n")
#
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print('\n')
# #
# for i in range(1,20001):
#     print(i)
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print('\n')
# for i in range(6, 0, -1):
#     for j in range(1, i + 1):
#         print('*', end=' ')
#     print('\n')

#
#
# for i in range(1, 6):
#     for k in range(1, 6 - i):
#         print(' ', end=' ')
#     for j in range(1, i + 1):
#         print('*', end='')
#     print('\n')
#     *
#    **
#   ***
#  ****
# *****

# for i in range(1, 6):
#     for k in range(1, 6 - i):
#         print(' ', end='')
#     for j in range(1, i + 1):
#         print('*', end='')
# #     print('\n')
# for i in range(1,30):
#     for k in range(1,25-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print('\n')

# for i in range(5,0,-1):
#     for k in range(1,6-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print('\n')

#* * * * *
# * * * *
#   * * *
#     * *
#       *

# while
# i=1
# while i<=10:
#     print(i)
#     i=i+1

# while Loop
# i=1
# while i<6:
#     password=input('enter your password')
#     i+i+1
#     print('limit exceded')

# fruits = ['apple', 'banana', 'orange', 'mango', ]
# for x in 'banana':
#     print(x)
#     if x == 'banana':
#         break
#     else:
#         print('we')

#
# test = ['red','big','tasty']
# fruites =['apple','banana','cherry']
# for x in test:
#     for y in fruites:
#         print(x,y)
#
# #
#
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry
#

# class MyClass:
#   x = 5
#
# p1=MyClass()
# print(p1.x)
# print(MyClass)
#

#
# class NewClass:
#     def __init__(self, name,group):
#         self.name =name
#         self.group = group
#
#
# n1=NewClass('owais','B')
# print(n1.name)
# print(n1.group)
#
# class NewClass:
#     def __init__(self, name, group):
#         self.name = name
#         self.group = group
#
#
# n1 = NewClass('owais', 'B')
# print(n1.name)
# print(n1.group)
# n2 = NewClass('ahmed', 'C')
# print(n2.name)
# print(n2.group)
#
#
# class Person:
#
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age
#
#     def myfunc(self):
#         print("Hello my name is " + self.name, "my age is ", self.age)
#
#
# p1 = Person("John", "36")
#
# print(p1.myfunc())

# class circle:
#   def _init_(self,radius):
#     self.radius=radius
#   def area(self):
#     self.area=3.14*self.radius**2
#     return self.area
#   def circumference(self):
#     self.circumference=2*3.14*self.radius
#     return self.circumference
# call=circle(5)
# print("THE AREA IS",call.area())
# print("THE CIRCUMFERENCE IS",call.circumference())


#
# class calculat:
#     def _init_(self, num):
#         self.number = num
#
#     def square(self):
#         self.squares = self.number ** 2
#         return self.squares
#
#     def cube(self):
#         self.cubes = self.number ** 3
#         return self.cubes
#
#
# call = calculat()
# print(call.square(3))
# print(call.cube(2))

#
# class Student:
#     # name="owais sikander"
#     college_name ='abcd college'
#     def __init__(self, name):
#         self.name = name
#         print('adding new student in database')
#
#
# student1 = Student('owais')
# print(student1.name)
#
#
# s2 =Student('khan')
# print(s2.name)
# print(s2.college_name)
# print(Student.college_name)

#
#
# class Faculty:
#     def putdata(self):
#         self.id=int(input('Enter your ID'))
#         self.name=input('Enter your name')
#         self.salary=float(input('Enter your salary'))
#     def display(self):
#         print('your id is',self.id)
#         print('your name is',self.name)
#         print('your salary is',self.salary)
#
# a=Faculty()
# a.putdata()
# a.display()

#
# class data:
#     def _init_(self, name, id, dept):
#         self.username = name
#         self.userid = id
#         self.userdept = dept
#
#     def display(self):
#         self.displayname = self.username
#         self.displayid = self.userid
#         self.displaydept = self.userdept
#         print(f"your name is {self.displayname} your id is {self.displayid} your dept is {self.displaydept}")
#
#
# student1 = data("hafiz", 20252039, "bcsc")
# print(student1.display())
# student2 = data("hunain", 16, "bcsc")
# print(student2.display())

# ITS CLASS
# class Car:
#   color="black"
#   weight="1000kg"
#   speed="100km/h"
#
# # ITS OBJ CREATE
# c1=Car()
# print(c1.color)
# print(c1.weight)
# print(c1.speed)
#
#
# # INIT METHOD and self
# class Students:
#
#   # defult constructor
#   def __init__(self):
#     pass
#
#   # class attr which is same
#   college_Name = "Jamia Millia Islamia"
#   name = "annonymous"
#
#   # parameterized constructor
#   def __init__(self, name, marks):
#     self.name = name  #its obj attr which change
#     self.marks = marks
#     print("add new student in dataBAse")
#
#   # method
#   def welcome(self):
#     print("welcome to JMI", self.name)
#
#
#   # method
#   def show_marks(self):
#     print("your marks is ", self.marks)
#
#
#
# s1 = Students("hafiz",98 )
# print(s1.name, s1.marks)
#
# s2 = Students("ali", 99)
# print(s2.name, s2.marks)
#
# print(Students.college_Name)  #FOR CLASS ATTR which is same
# print(s2.college_Name)
#
# print(s2.name)
# print(Students.name)
#
# print(s2.welcome())
# print(s2.show_marks())


# class Faculty:
#     def dataput(self):
#         self.id = int(input('Enter you ID'))
#         self.name = input('Enter you name')
#         self.salary = float(input('Enter you ID'))
#     def display(self):
#         print('your id is ',self.id)
#         print('your name is',self.name)
#         print('your salary is',self.salary)
#
# f1=Faculty()
# f1.dataput()
# f1.display()


# class Faculty:
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#     def display(self):
#         print('your id is',self.id)
#         print('your name',self.name)
#         print('your salary',self.salary)
# m1=Faculty(12,'owias',22222)
# print(m1.display())
