#Find Duplicate Elements
#Write a program to find duplicate elements in a list.
my_list = [1, 2, 3, 4, 5, 2, 3, 6]
duplicates = set()
for item in my_list:
    if my_list.count(item) > 1:
        duplicates.add(item)
print("Duplicate elements:", duplicates)  
