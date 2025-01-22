# <------------------------------DAY-1---------------------------------------------->
# q1.program to add two numbers
# print("hello world!")
# a=int(input("enter no.: "))
# b=eval(input("enter 2no.: "))
# sum=a+b
# print("sum= ", sum)
#import math

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

test="Hello world! This is a string"
print(test.count("Hello"))
print((test.index("Hello")))
print((test.index("world")))
# print(test.index("World",start=0))
# print(test.index("Hello",start=0))
print(test.lower())
print(test.upper())
words=test.split()
print(words)
joined="  ".join(words)
print(joined)
print(test.replace("Hello", "Hello World"))
print(test.find("Hello"))
print(test.find("world"))
print(test.startswith("Hello"))
print(test.endswith("World"))