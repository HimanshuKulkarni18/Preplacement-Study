#1. What is the difference between append() and extend()?
append() adds a single element
extend() adds multiple elements
a = [1, 2]

a.append(3)
print(a)

a.extend([4, 5])
print(a)

Output:

[1, 2, 3]
[1, 2, 3, 4, 5]

#2. Difference between remove(), pop(), and del?
Method	Purpose
remove()	Removes value
pop()	Removes using index
del	Deletes element/object

Example:

nums = [10, 20, 30]

nums.remove(20)
print(nums)

nums.pop(0)
print(nums)

#3. What is a dictionary?

Dictionary stores data in key-value pairs.

student = {
    "name": "Rahul",
    "age": 21
}

print(student["name"])

#4. What is a set in Python?

A set is an unordered collection of unique elements.

s = {1, 2, 2, 3}
print(s)

Output:

{1, 2, 3}

#5. What is the difference between sort() and sorted()?
sort()	sorted()
Changes original list	Returns new list
Works only on lists	Works on all iterables
nums = [3, 1, 2]

print(sorted(nums))
print(nums)

nums.sort()
print(nums)

#6. What is slicing in Python?

Extracting part of a sequence.

text = "Python"

print(text[0:3])

Output:

Pyt

#7. What is the difference between local and global variables?
Local variable → inside function
Global variable → outside function
x = 10

def demo():
    y = 5
    print(x)
    print(y)

demo()

#8. What is break statement?

Stops the loop immediately.

for i in range(5):
    if i == 3:
        break
    print(i)

#9. What is continue statement?

Skips current iteration.

for i in range(5):
    if i == 2:
        continue
    print(i)

#10. What is pass statement?

Placeholder statement that does nothing.

for i in range(5):
    pass
#11. What is None in Python?

None represents absence of value.

x = None
print(x)

#12. What are Python keywords?

Reserved words with special meaning.

Examples:

if
else
while
for
class
return

#13. What is type casting?

Converting one datatype into another.

x = "10"

print(int(x) + 5)

#14. What is the use of len()?

Returns length of object.

name = "Python"

print(len(name))

#15. What is range() in Python?

Generates sequence of numbers.

for i in range(1, 5):
    print(i)

#16. What is enumerate()?

Adds index while looping.

names = ["A", "B", "C"]

for index, value in enumerate(names):
    print(index, value)

#17. What is zip() function?

Combines multiple iterables.

a = [1, 2]
b = ["A", "B"]

print(list(zip(a, b)))
#18. Difference between mutable and immutable objects?
Mutable	Immutable
Can change	Cannot change
List, dict	String, tuple

#19. What is a generator?

Generator produces values one at a time using yield.

def demo():
    yield 1
    yield 2

g = demo()

print(next(g))
print(next(g))
#20. What is a decorator?

Decorator modifies function behavior.

def decorator(func):
    def wrapper():
        print("Before function")
        func()
    return wrapper