#Write a program to count the number of vowels in a given string.
s = "Himanshu Kulkarni!"
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count +=1 
print("The number of vowels in the string is:", count)