#Lambda Function
# jatin = lambda a,b,c:a+b+c
# print(jatin(4,3,6))

# # var = lambda x:x / 2
# # print(var(42))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))



# Arrays:python doesnot have inbuilt support for Array, Instead of that we use list 
# crushNames = ['Vish','Dilli','Anju']
# print(crushNames[2])
# print(len(crushNames))
# crushNames.append("ja")
# crushNames.pop()
# crushNames.remove('Anju')
# for i in crushNames:
#     print(i)


# Python classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# class first:
#     c = 30
# o1 = first()
# print(o1.c)

# All classes have a function called __init__()
# class future:
#     def __init__(jack,car, ploats):
#         jack.car = car
#         jack.ploat = ploats

#     def check(self):
#         print(f"Lyo Run ho gaya... aur mera pas total {self.ploat} ploats hai")

# p1 = future('Audi',59)
# print(p1.car)
# print(p1.ploat)
# p1.check()
# p1.ploat = 435
# p1.check()
# del p1.ploat
# try(AttributeError a):
#     p1.check()
# throw:print('yes')
    

#Inheritance in python

# class person:
#     def __init__(self,firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class student(person):
#     def __init__(self, firstname, lastname,year):
#         super().__init__( firstname, lastname)
#         self.graduationyear = year
#         #add properties etc..
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# x = student("Jatin","Mewada",2000)
# x.printname()
# x.welcome()


# #python Iterators
# mytup = ("jatin","Umar","Akash")
# myit = iter(mytup)
# str = "jatinmewadaisgoodcodder"
# print(next(myit))
# print(next(myit))
# print(next(myit))
# for i in str:
#     print(i)


#Scope in python


# x = 899
# def myfun():
#     # x = 290
#     def myinner():
#         global x
#         x =99
#         print(x)
#     myinner()
# print(x)
# myfun()