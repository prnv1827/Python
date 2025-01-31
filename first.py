# <------------------------------DAY-1---------------------------------------------->
# q1.program to add two numbers
# print("hello world!")
# a=int(input("enter no.: "))
# b=eval(input("enter 2no.: "))
# sum=a+b
# print("sum= ", sum)
#import math
from importlib.resources import contents

from anaconda_project.internal.conda_api import result
from sympy import content

#Q2.)program to make fxn to add two numbers
# def add(a,b):
#     return (a+b)
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# print(add(a,b))

#Q3.)program to find area of triangle using herons formula
# a=int(input("enter no.: "))
# b=int(input("enter 2no.: "))
# c=int(input("enter 2no.: "))
# s=(a+b+c)/2
# print(s)
# s1=math.sqrt(s*((s-a)*(s-b)*(s-c)))
# print((s1))

#Q4.)program to swap two numbers
# a=int(input("enter no.: "))
# b=int(input("enter 2no.: "))
# a=a*b
# b=a//b
# a=a//b
# print(a,b)

#Q5.)program to convert celsius to fahrenheit
# a=float(input("enter celsius: "))
# c=(a*9/5)+32
# print("The temperature in fahrenheit is: ",c)

#Q6.)program to convert fahrenheit to celsius
# f=float(input("enter fahrenheit: "))
# c=(a-32)*5/9
# print("The temperature in celsius is: ",c)

#Q7.)program to calculate Simple interest
# P=float(input("enter P: "))
# R=float(input("enter R: "))
# T=float(input("enter T: "))
# SI=(P*R*T)/100
# print(SI)

#Q8.)program to calculate surface area of cylinder(2 pi r h+2 pi r^2)
# pi=3.14
# r=int(input("Enter radius: "))
# h=int(input("Enter height: "))
# area=(2*pi*r)*(h+r)
# print("Surface area of cylinder is: ",area)

#Q9.)program to find hypotenuse
# import math
# p=int(input("Enter perpendicular: "))
# b=int(input("Enter base: "))
# h=math.sqrt((p*p+b*b))
# print("Hypotenuse is: ",h)

#Q10.)program to find compound interest(A=P(1+(r/100)^t)
# p=int(input("Enter P: "))
# r=int(input("Enter r: "))
# t=int(input("Enter t: "))
# CI=p*((1+(r/100))**t)-p
# print("Compound Interest is ",CI)

#Q11.)program to find avg of 3 numbers
# a=int(input("Enter A: "))
# b=int(input("Enter B: "))
# c=int(input("Enter C: "))
# avg=(a+b+c)//3
# print("Average is ",avg)

#Q12.)program to calculate sum of 5 subjects marks and find percentage
# a=int(input("Enter Hindi marks: "))
# b=int(input("Enter English marks: "))
# c=int(input("Enter Maths marks: "))
# d=int(input("Enter computer marks: "))
# e=int(input("Enter science marks: "))
# percentage=((a+b+c+d+e)/500)*100
# print("Percentage of 5 subjects are: ",percentage,"%")

#Q13.)program to find gross salary
# a=int(input("Enter salary: "))
# Annual_Income=a*12
#gross_salary=a*12
# print("Annual income is ",Annual_Income)

#Q14.)program to find area of circle
# import math
# r=int(input("Enter radius: "))
# area=math.pi*(r*r)
#alternative=math.pi(math.pow(r,2)
# print("Area of circle is: ",area)

#Q15.)program to find area of rectangle
# l=int(input("Enter length: "))
# b=int(input("Enter breadth: "))
# area=l*b
# print("Area of rectangle is: ",area)

#Q16.)program to find area of square
# s=int(input("Enter side: "))
# area=math.pow(s,2)
# print("Area of square: ",area)

#Q17.)program to find perimeter of circle
# import math
# r=int(input("Enter radius: "))
# perimeter=2*math.pi*r
# print("Perimeter of circle is: ",perimeter)

#Q18.)Program to find area of scalene triangle
# b=int(input("Enter base: "))
# h=int(input("Enter height: "))
# area=1/2*b*h
# print("Area of scalene triangle is: ",area)

#Q19.)program to find area of trapezium
# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# h=int(input("Enter height: "))
# area=(a+b)/2*h
# print("Area of trapezium: ",area)

#Q20.) program to find area of right angled triangle
# b=int(input("Enter base: "))
# h=int(input("Enter height: "))
# area=1/2*b*h
# print("Area of right angeled triangle is: ",area)

#<---------------------------------------DAY-2----------------------------------------------->

#IDENTIFIERS AND KEYWORDS
# _var=4
# print(_var)

# x=10
# name="Pranav"
# pi=4.13
# print(x,name,pi)

#DATATYPES
# z=3+7j
# print(typeof(z))

# my_list=[1,2,3]
# my_tuple=(1,2,3)
# my_range=range(5)
# print(my_range)
# print(my_list, my_tuple)

# for i in range(0,10,2):
#     print(i)
# for j in range(10,0,-2):
#     print(j)

# for i in range(100,0,-20):
#     print(i)

# my_dict={"Name": "Alice", "Age":18}
# print(my_dict)
# print(my_dict["Name"])
# print(my_dict["Age"])

#####SET##########
# my_set={1,2,3}
# print(my_set)
# my_forzenset=frozenset([1,2,3])
# print(my_forzenset)

#####NONE TYPE##########
# nothing=None
# print(nothing)

###############implicit and explicit(TYPE CONVERSION)#################
# x="3"
# y=4.5
# z=int(x)+y
# print(z)

##########Operators and operands##############
##ARITHEMATIC OPERATORS + - * / // %
# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# sum=a+b
# print(sum)
# sub=a-b
# print(sub)
# mul=a*b
# print(mul)
# div=a/b
# print(div)
# mod=a%b
# print(mod)
# floordiv=a//b
# print(floordiv)

#####COMPARISON/relation(== < > <= >= !=)
# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a<=b)
# print(a>=b)

##########logical operator
# a=True
# b=False
# print(a and b)
# print(a or b)
# print(not a)

####BITWISE OPERATORs(& | ^ ~ << >>)
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)
# print(a<<b)
# print(a>>b)

#######Assignment operator(= += -= *= /= %= //=)
# a=7
# print(a)
# a+=7
# print(a)
# a-=7
# print(a)
# a*=7
# print(a)
# a/=7
# print(a)
# a%=7
# print(a)
# a//=7
# print(a)
# a**=7
# print(a)
# b=7
# b**=7
# print(b)

#SPECIAL OPERATORS
#is and is not
# x=[1,2,3]
# y=[1,2,3]
# z=x
# print(x is y)
# print(x is z)
# print(x is not y)

######MEMBERSHIP OPERATOR(in and notin)
# print('x' not in 'apple')

#<------------------------------DAY-3-------------------------->
#EXPRESSION 1.Constant
# result=5+9
# print(result)

#ARITHEMATIC EXPRESSION
# a=5
# b=6
# print(a+b)
# print(a and b) #prints value of b
# print(a or b) #prints value of a
# print(a<b)
# print(a>b)
# print(a&b) #binary mee convert karke "and"
# print(a|b) #binary mee convert karke "or"
# print("Hello World"+" Python is a programming language")
# str1="Hello World"
# str2=(" Python is a programming language")
# str3=str1+str2
# print(str3)

#STRING OPERATION
# s1="Hello"
# print(s1)
# s2='alice'
# print(s2)

#MUTLI-LINE STRING
# s3='''This is a
# multiline
# string'''
# print(s3)
# print(s3[11])
#SLICING (START,STOP,STEP)
# s4="Hello this is a string"
# print(s4[0:6])
# print(s4[:6])
# print(s4[7:])
# print(s4[0:11:2])
# print(s4[::2])
# print(s4[::-1])
# s5="Python is awesome. Python is easy to use."
# print(s5[0:12:3])
# print(s5[0:4])
# print(s5[::2])
# print(s5[:6])
# print(s5[6:])

#STRING FORMATTING
# name="Pranav"
# age=18
# profession="Programmar"
# print("my name is {} and I am {} years old. And my profession is {}".format(name,age,profession))
# #use of F string
# print(f'My name is {name} and I am {age} years old.')
# #use of % operator (old method)
# print("My name is %s and I am %d years old."%(name,age))

#BASIC OPERATIONS AND METHODS ON STRING
# s1="Hello"
# s2="World"
# print(s1+s2)
# print(s1*7)

# test="Hello world! This is a string"
# print(test.count("Hello"))
# print((test.index("Hello")))
# print((test.index("world")))
# # print(test.index("World",start=0))
# # print(test.index("Hello",start=0))
# print(test.lower())
# print(test.upper())
# words=test.split()
# print(words)
# joined="  ".join(words)
# print(joined)
# print(test.replace("Hello", "Hello World"))
# print(test.find("Hello"))
# print(test.find("world"))
# print(test.startswith("Hello"))
# print(test.endswith("World"))

#LIST, TUPLE AND DICTIONARY
# my_list=[1,2,3,4,"Pranav","Singh",99.9]
# print(my_list)
# my_list[0]=5
# print(my_list)
# my_tuple=(1,2,3,4,"Pranav","Singh",99.9)
# print(my_tuple)
# my_set={1,2,3,4,1}
# print(my_set)
# my_dict={"name":"Pranav Singh","age":18,"city":"Greater Noida","city":"Greater Noida"}
# print(my_dict)

# str1=("Apple")
# a=str1.count('p')
# print(a)

#<--------------------------DAY-5---------------------------->
#loops(for loop, while loop, do-while, for-else)
# i = 1
# a = ++i
# b = i+1
# print(a,b, a-b)

# for i in range(1,11):
#     print("2 *", i, "=", 2*i)

# for i in range(10):
#     print(i)
# else:
#     print("Loop finished")

#NESTED FOR LOOP
# for i in range(10):
#     for j in range(10):
#         print(f"i={i}:j={j}")

#USE OF BREAK and CONTINUE AND PASS STATEMENT
# for i in range(10):
#     if i==3:
#         continue
#     print(i)
#
# for i in range(10):
#     if i==3:
#         break
#     print(i)

# for i in range(10):
#     if i==3:
#         pass
#     print(i)

#ITERATION OVER LIST
# fruits=["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)

#PATTERN
# n=4
# for i in range(1,n):
#     print(" "*(n-i) + "*"*i)
#
# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(n,end="")
#         n+=1
#     print()
#
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

#Triangle
# n=4
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "* i)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(65+j-1),end="")
#     print()

# n=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         for k in range(j+1):
#             print(" "*(k)+chr(66+k-1),end="")
#     print()

#ARMSTRONG NUMBER
# n=int(input("Enter a number: "))
# s=0
# no=n
# while n!=0:
#     digit=n%10
#     s+=digit**3
#     n//=10
# if s==no:
#     print("Armstrong number")
# else:
#     print("Not armstrong number")

#PALINDROME NUMBER
# n=int(input("Enter a number: "))
# no=n
# rev=0
# while n>0:
#     digits=n%10
#     rev=rev*10+digits
#     n=n//10
# if rev==no:
#     print("Palindrome")
# else:
#     print("not Palindrome")

#print even or odd series upto 40
# print("even numbers till 40:-")
# for i in range(2,41,2):
#     print(i,end=" ")
# print("odd numbers till 40:- ")
# for i in range(1,41,2):
#     print(i,end=" ")
# print("number divisible by 7")
# for i in range(0,100):
#     if i%7==0:
#         print(i,end=" ")

#MAGIC NUMBER
# n=int(input("Enter number: "))
# while n>9:
#     s=0
#     while n > 0:
#         s += n % 10
#         n //= 10
#     n=s
# if n==1:
#     print(n,"is a magic number")
# else:
#     print(n,"is not a magic number")
# if n%9==1:
#     print("magic")
# else:
#     print("not magic")

#<---------------------------------------DAY-6---------------------------------->
# def sum(a,b):
#     return (a+b)
# x=eval(input("Enter a number: "))
# # print(abs(x))
# print(sum(x,5))

# x=int(input("Enter number: "))
# print(abs(x))

# import math
# x=float(input("Enter a number: "))
# y=int(input("Enter another number: "))
# a=(1,2,3,4)
# print(abs(x))
# z=sum(a)
# print(z)
# print(math.ceil(x))
# print(math.floor(x))
# print(math.sqrt(y))
# print(round(x,2))

# num=[2,4,5,1,234,45]
# ln=max(num)
# print(ln)
# sn=min(num)
# print(sn)
# total=sum(num)
# print(total)
# str_num="42"
# print(str_num)
# convert_to_int=int(str_num)
# print(convert_to_int)
# num1=convert_to_int
# convert_to_float=float(str_num)
# print(f"Int number is: {convert_to_int}\n" f"converted to float{convert_to_float}")
#
# unsorted_number=[5,3,8,1,2]
# sorted_number=sorted(unsorted_number)
# print(f"sorted list is:{sorted_number}")
#
# start=1
# stop=10
# step=2
# no_seq=range(start,stop,step)
# print(f"The range from {start} to {stop}" f" with a step of {step} is:{no_seq}")

#WAP to make a fxn of even and odd
# def even_odd(a):
#     if a%2==0:
#         return ("even")
#     else:
#         return ("odd")
# x=int(input("a: "))
# print(even_odd(x))

#WAP to find highest common factor
# import math
# def hcf(a,b):
#     return math.gcd(a,b)
# a=int(input("enter a: "))
# b=int(input("enter b: "))
# print(hcf(a,b))

# str1=input("Enter elements seperated by spaces: ")
# my_list=str1.split()
# my_list=[int(x) for x in my_list]
# print("list: ",my_list)

#<--------------------------DAY-7------------------------------->
# x=10#GLOBAL VARIABLE
# def sum():
#     y=20#LOCAL VARIABLE
#     return x+y
# print(sum())

# x=20
# def sum():
#     y=20
#     def f():
#         nonlocal y
#         y+=10
#         # z=y+10
#         print(f"non-local y: {y}")
#     f()
#     print(f"global x: {x}")
# sum()

#RECURSION
# def fact(num):
#     if num==0:
#         return 1
#     else:
#         return num*fact(num-1)
# n=int(input("Enter a  number: "))
# f=fact(n)
# print("The factorial of {} is {}".format(n,f))

#FIBONACCI SERIES
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# num=int(input("Enter a number: "))
# for i in range(num):
#     print(fib(i),end=" ")

#USE OF LAMBDA FXN
# result=lambda n1, n2: n1+n2
# print(result(1,2))
# print(result(1,54))

# num=[1,2,3,4,5,6,7,8,9]
# def is_even(n):
#     if n%2==0:
#         return True
# even_num=filter(is_even,num)
# even_num_list=list(even_num)
# print(even_num_list)

# num=[1,2,3,4,5,6,7,8,9]
# even_num=filter(lambda x: x%2==0, num)
# even_num_list=list(even_num)
# print(even_num_list)

# list=[10,5,12,78,6,1,7,9]
# for i in list:
#     print(i**3)

# liist=[10,5,12,78,6,1,7,9]
# cube_list=list(map(lambda x:x**3, liist))
# print(cube_list)

# radii=[0.5,5.44,2,33,4,6,7,8.95]
# # for i in radii:
# #     z=i**2
# area=list(map(lambda x:3.14*x**2, radii))
# print(area)

#WAP to find area of rhombus on a list
# l1=[2,3,4,5,6,7,8,9]
# y=int(input("Enter second diagonal: "))
# area=list(map(lambda x:x*y, l1))
# print(area)

# l1=[2,3,4,5,6,7,8,9]
# l2=[1,2,3,4,5,6,7,8]
# area=list(map(lambda x,y:0.5*x*y, l1,l2))
# print(area)

#from functools import reduce
# num_list=[10,5,12,78,6,1,7,9]
# large=reduce(lambda x,y: x if x>y else y, num_list)
# print(large)
# total_sum=reduce(lambda x,y:x+y, num_list)
# print(total_sum)

#WAP TO FIND ALL NUMBRS DIVISIBLE BY 3 AND 5 IN A LIST USING A LAMBDA FXN
# liist=[15,30,22,45,50,60,70,80,75,90,100]
# divv=list(filter(lambda x:x%3==0 and x%5==0 , liist))
# print(divv)

#USE map() to convert a list of temp from celsius to fahrenehit
# liist=[0,10,20,30,40,50,60,70,80,90,100]
# temp=list(map(lambda x:x*1.8+32, liist))
# print(temp)

#WAP TO FILTER OUT -VE NUMBER
# liist=[2,-6,9,6,-7,45]
# nega=list(filter(lambda x:x<0, liist))
# print(nega)

#WAP to caluculate sum of squares of all numbers in a list using reduce()
# from functools import reduce
# liist=[2,2,3,4]
# sos=reduce(lambda x,y:x+y**2, liist,0)
# print(sos)

#With the help of reduce() find max element in list
# from functools import reduce
# l1=[1,34,57,79,3,56]
# l2=reduce(lambda x,y:x if x>y else y, l1)
# print(l2)

#WAP to find prime
# def is_prime(number):
#     if number<2:
#         return False
#     for i in range(2, int(number**0.5)+1):
#         if number%i==0:
#             return False
#         return True
# numbers_list=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# prime_number_list=list(filter(is_prime, numbers_list))
# print("Prime numbers list:",prime_number_list)

#<---------------------------------------DAY-8-------------------------------------------------->
# import math
# result=math.sqrt(12)
# print(result)
#
# from math import *
# result=math.sqrt(12)
# print(result)
# print(pi)
# print(result)
# print(sin(0))

# import mymodule
# n1=int(input("Enter a number: "))
# n2=int(input("Enter second number: "))
# print(mymodule.add(n1,n2))
# print(mymodule.sub(n1,n2))
# print(mymodule.mul(n1,n2))


# from mymodule import add,PI
# n1=int(input("Enter number: "))
# n2=int(input("Enter second number: "))
# print(mymodule.add(n1,n2))
# print(PI)

# import random
# print(random.randint(1,20))
# print(random.random())
# print(random.choice(['Apple','Banana','Cherry','Strawberry']))

#<---------------------------------DAY-9------------------------------------------->
#SEQUENCES
#1.)STRING
#PACKING
# packed=1,2,3,4
# print(packed)

# UNPACKING
# x,y,z=10,20,30
# print(x,y,z)

# USING * TO COLLECT REMAINING ITEMS
# *a,b=[1,2,3]
# print(a,b)

# def return_multiple_values():
#     return 1,2,3
# val1,val2,val3=return_multiple_values()
# print(val1)
# print(val2)
# print(val3)

#MUTABLE SEQUENCES
#1.)LIST
# list=[1,2,3,4,5]
# list.append(6)
# print(list)
# list[1]=7
# print(list)

#IMMUTABLE SEQUENCES
#2.)STRING
# text="hello"
# # text[0]='p'
# text="pranav"
# print(text)

#3.)TUPLE
# t=(1,2,3,4)
# # t[0]=1
# t=(1,2,3,4,5)
# print(t)

#STRING ADVANCED METHODS
# print("hi world".capitalize())
# print("HI WORLD".casefold())
# print("HI WORLD".lower())
# print("hi world".upper())
# print("hi world".title())
# print("hELLO WORLD".swapcase())
# print("Hello World".find("d"))
# print("Hello".rfind("l"))
# print("Hello World".index("l"))
# print("Hello World".count("l"))
# print("Hello World".replace("l","e"))
# print("Hello,World".split(","))
# print("Hello,World,Test".rsplit(",",2))
# print("Hello\nWorld".splitlines())
# print("    Hello".strip())
# print("    Hello".lstrip())
# # print("    Hello     ".rstrip())
# print("Hello World".rsplit("e",1))
# print("Hello World".startswith("e"))
# print("Hello World".startswith("He"))
# print("Hello World".endswith("e"))
# print("Hello World".endswith("ld"))
# print(",".join(["a","b","c"]))
# print("abc".isalpha())
# print("abc".isnumeric())
# print("abc1234".isalpha())
# print("1234".isdigit())
# print("123abc".isdigit())
# print("123abc".isalnum())
# print("123".isalnum())
# print(" ".isspace())
# print(" a".isspace())
# print("a".isspace())
# print(" a ".isspace())
# print(len(" Hello World "))
# print("Hello,{}".format("World"))
# print("42".zfill(5))
# print("Hello".center(10))
# print("Hello".ljust(10))
# print("Hello".rjust(10))
# name="Alice"
# age=22
# print(f"Name: {name}, Age: {age}")

#LIST
#CREATE A LIST OF SQAURES
# squares=[x**2 for x in range(1,10)]
# print(squares)

# #CREATE A LIST OF CUBES
# cubes=[x**3 for x in range(1,10)]
# print(cubes)

# #FOR EVEN NUMBERS
# even=[x for x in range(1,10) if x%2==0]
# print(even)
#
# #ODD NUMBERS
# odd=[x for x in range(1,10) if x%2!=0]
# print(odd)

#DEMONSTRATE HOW TO UNPACK SQUENCES WITH * (eg. Head, *middle, tail)
# seq=[1,2,3,4]
# head,*middle,tail=seq
# print("head",head)
# print("middle",*middle)
# print("tail",tail)

#LIST MODULE
# list=[1,2,3]
# list.append(4)
# print(list)
# list.extend([5,6])
# print(list)
# list.insert(2,7)
# print(list)
# list.remove(4)
# print(list)
# list.pop(1)
# print(list)
# list.clear()
# print(list)

# list2=[1,2,3]
# print(list2.index(2))
# print(list2.count(1))
# list4=[2,4,1,3,56,46,57,54]
# list4.sort()
# print(list4)
# list4.reverse()
# print(list4)
# new_list=list4.copy()
# print(new_list)

#WAP to convert list of strings to uppercase and remove duplicated using list comprehensions
# lst=['hello','world','hello','world']
# lst1=[s.upper() for s in lst]
# print(lst1)
# lst2=[]
# for s in lst1:
#     if s not in lst2:
#         lst2.append(s)
# print(lst2)

# s="1,2,3,4"
# a=s.split(',')
# lst=[]
# for i in a:
#     lst.append(int(i))
# print(sum(lst))

# WAP TO DEMONSTRATE DIFF B/W SHALLOW AND DEEP COPIES OF LIST CONTAINING TUPLES
# original_list=[(1,2),(3,4),[4,5],(5,6),(6,7),(7,8),(8,9),(9,10),(11,12),(12,13),(14,15)]
# shallow_copy= copy.copy(original_list)
# deep_copy= copy.deepcopy(original_list)
# original_list[2][1]=99
# print("original list: ",original_list)
# print("shallow list: ", shallow_copy)
# print("deep copy: ",deep_copy)

#METHOD 2
# original_list=[(1,2),(3,4),[4,5]]
# shallow_copy= original_list[:]
# deep_copy= copy.deepcopy(original_list)
# original_list[2][0]=99
# print("original list: ",original_list)
# print("shallow list: ", shallow_copy)
# print("deep copy: ",deep_copy)

#METHOD 3
# original_list=[(1,2),(3,4),[4,5]]
# shallow_copy= original_list[:]
# deep_copy= json.loads(json.dumps(original_list))
# original_list[2][0]=99
# print("original list: ",original_list)
# print("shallow list: ", shallow_copy)
# print("deep copy: ",deep_copy)

#TUPLES
# tuple=(1,2,3)
# print(tuple)
# print(type(tuple))
# print(tuple.count(2))
# print(tuple.index(3))

#PACKED AND UNPACKED
# packed=1,2,3
# print(packed)
#
# x,y,z=packed
# print(x,y,z)

#SUM AND PRODUCT USING PACKED
# def sum_and_product(a,b):
#     return a+b, a*b
# result_sum, result_product=sum_and_product(4,5)
# print(result_sum, result_product)

#FILTERING
# odd_squares=[x**2 for x in range(1,11) if x%2!=0]
# print(odd_squares)

#ADVANCED STRINGS
# text="Hello Python"
# vowels=[char for char in text.lower() if char in 'aeiou']
# print(vowels)

#<-----------------------------------------DAY-10------------------------------->
#SETS AND DICTIONARY
#EMPTY SETS
# empty_set=set()

#non empty set
# my_set={1,2,3}
# print(my_set)

#from a list
# set_from_list=set([1,2,3])
# print(set_from_list)

#SET MODULE
# my_set.add(4)
# print(my_set)
# my_set.remove(4)                #generates error when element not found
# print(my_set)
# my_set.discard(4)               # does not generate error when element not found
# print(my_set)

# set1={1,2,3}
# set2={1,2,3,4,5}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issuperset(set2))
# print(set1.issubset(set2))

#REGULAR EXPRESSION
# print(re.match("a.b","a.bc"))
# print(re.search("cat","cat is here"))
# print(re.findall("\d+","A123B456"))
# print(re.sub("\s","-","Hello World"))

# pattern=r"\d+"
# text="My age is 18 and yours is 30"
# print(re.findall(pattern,text))
# print(bool(re.match(r"Hello","Hello World")))
# pattern=r"\s"
# print(re.sub(pattern,"-",'Hello World'))


# WAP TO EXTRACT ALL EMAIL ADDRESS FROM A GIVEN TEXT
# import re
#
# text = """Contact us at support@example.com or sales@example.com
# You can also reach out to john.doel@example.com"""
# email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# emails = re.findall(email_pattern, text)
# print(emails)

#<---------------------DAY-12--------------------------->

#FILE HANDLING AND EXCEPTION MANAGEMENT(1.r-read op. 2.)w-write op. 3.)a-append 4.)r+-read and write op)
# file=open('test.txt','r')
# file.close()
# file=open('test.txt','w')
# file.close()

# with open('test.txt','w') as f:
#     f.write('hello')
#     f.write(' world')
#     f.write('\n')
#     f.write("This is a file handling test case")
#     f.close()
#
# #READING AN ENTIRE FILE
# with open('test.txt','r') as f:
#     content=f.read()
#     print(content)
#
# #READING LINE BY LINE
# with open('test.txt','r') as f:
#     for line in f:
#         print(line.strip())
#
# #READING SPECIFIC NUMBER OF CHARACTER
# with open('test.txt','r') as f:
#     content=f.read(10)
#     print(content)
#
# #APPEND TO A FILE
# with open('test.txt','a') as f:
#     f.write('\nThis line is appended')
#
# with open('test.txt','r') as f:
#     content=f.read()
#     print(content)

import os

from twisted.conch.ssh.connection import value

# current_dir=os.getcwd()
# print(current_dir)
# os.chdir("C:\Program Files")
# print("Changed Directory:",os.getcwd())

# os.mkdir("Test")           #mkdir is used to creater directories(file)
# contents=os.listdir(".")
# print("Directory contents:",contents)

# os.rmdir("Test")     #remove directory

#DIRECTORY TRAVERSAL
# for root,dirs,files in os.walk('.'):
#     print("ROOT",root)
#     print("DIRS",dirs)
#     print("FILES",files)

#UNHANDLED EXCEPTION EXAMPLE
# try:
#     num=int(input("Enter a number: "))
#     result=10/num
#     print("Result:",result)
# except ZeroDivisionError:
#     print("Error: Zero division not allowed")
# except ValueError:
#     print("Error: Invalid input. Please try again.")

# def check_age(age):
#     if age<18:
#         raise ValueError('age must be greater than 18')
#     print("Valid")
# try:
#     check_age(16)
# except ValueError as e:
#     print("Exception",e)

#ASSERTION EXAMPLE
# num=10
# assert num>0, "Number must be +ve"
# try:
#     with open("test.txt",'r') as f:
#         content=f.read()
#         words=content.split()
#         print("Word count:",len(words))
# except FileNotFoundError:
#     print("File not found")
#
# import math
# try:
#     num1=float(input("Enter the first number: "))
#     if num1<0:
#         raise ValueError("Cannot calculate sqrt of -ve number")
#     print("The sqrt of",num1,"is",math.sqrt(num1))
# except ValueError as e:
#     print("Error",e)

# try:
#     with open("test.txt",'r') as f1, open('test1.txt','r') as f2:
#         content=f1.read()
#         content2=f2.read()
#     with open('merged text','w') as f3:
#         f3.write(content+"\n"+content2)
#     print("File merged successfully")
# except FileNotFoundError as e:
#     print("File not found")
























