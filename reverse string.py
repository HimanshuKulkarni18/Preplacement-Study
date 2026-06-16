#Write a program to reverse a given string without using built-in reverse functions.
s = "Mahesh Joshi!"
reversed_string = ""
for char in s:
    reversed_string = char + reversed_string
print("The reversed string is:", reversed_string)