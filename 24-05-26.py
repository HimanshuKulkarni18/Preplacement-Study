#Basics
# 
# #1. Print "Hello, World!"
print("Hello, World!")

#2. Take a user's name as input and print a greeting
name=input("please enter your name:")
print("hello,"+name+"!")

#3. Add two numbers entered by the user
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
sum=num1+num2
print("the sum is:",sum)

#4 Find the area of a rectangle
length=float(input("enter length:"))
width=float(input("enter width:"))
area=length*width
print("the area of the rectangle is:",area)

#5.Convert Celsius to Fahrenheit.
celsius=float(input("enter temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print("the temperature in fahrenheit is:",fahrenheit)

#6.Swap two variables
a=input("enter value for a:")
b=input("enter value for b:")
a=b,b=a #swapping
print("after swapping a:",a)
print("after swapping b:",b)

#7. Check whether a number is even or odd
number=int(input("enter a number:"))
if number % 2 == 0:
    print("the number is even.")
else:
    print("the number is odd.")
    
# 8. Find the largest of three numbers
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
num3=float(input("enter third number:"))   
if num1 >= num2 and num1 >= num3:
    largest=num1
elif num2 >= num1 and num2 >= num3:
    largest=num2
else:    largest=num3
print("the largest number is:",largest)   

#9.Check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
#10. Calculate simple interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest per year: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

#Conditions and Loops

#1. Print numbers from 1 to 100 using a loop
for i in range(1, 101):
    print(i)
    
#2Print the multiplication table of a number.
num = int(input("Enter a number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
#3.Find the factorial of a number.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print("Factorial of", num, "is 1.")
else:    
    for i in range(2, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial) 
    
#4.Reverse a number.
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed number:", rev)

#5.Count digits in a number.
n = int(input("Enter a number: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Number of digits:", count)

    
    
    