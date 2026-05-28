#Python Q/A 

#1. Check whether a number is a palindrome

n = int( input ( "Enter the number" ) )
original = n
rev = 0
while
    n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if original == rev:
    print ( " it is Palindrome " )
else:
    print ( " it is not Palindrome " )

#2.Check whether a number is prime

n = int ( input ("Enter The Number"))
if n < 2
    prime = False
    else:
    prime = true 
i in range ( 2, int ( n**0.5)+1)
    n % 1 =0:
    prime = False:
    break 
print ("prime" if "prime" else "not prime")

#3.Print all prime numbers between 1 and 100

print ( "primes of 1 to 100" )
for num i range ( 2,101 ):
    prime = True
else 
    prime = False 
i in range ( 2, int ( n**0.5)+1)
    n % 1 = 0:
    prime false :
break 
if prime:
    print(num,end='')
print()

#4 Find the sum of digits of a number

n = abs(int(input("Enter a number: ")))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits =", total)

#5 Generate the Fibonacci sequence 

n = int(input("How many terms? "))
if n <= 0:
    print("Enter a positive integer.")
elif n == 1:
    print("0")
else:
    a, b = 0, 1
    print("Fibonacci:", a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()

#STRING 

#1. Count vowels in a string

s = input("Enter a string: ")
vowels = "AEIOUaeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Vowels =", count)

#2. Reverse a string

s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)
