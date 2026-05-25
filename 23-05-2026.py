23-05-2026
#Python 25 interview theory questions and answers
#5 Coding Q/A 
1. What is Python?
Python is a high-level, interpreted, and easy-to-learn programming language created by Guido van Rossum.

2. Is Python compiled or interpreted?
Python is an interpreted language.
The code is first converted into bytecode and then executed by the Python interpreter.

3. Why is Python popular?
Python is popular because:
	•	Easy syntax
	•	Readable code
	•	Large community
	•	Huge libraries support
	•	Cross-platform support

4. What are variables in Python?
Variables store data values.

name = "Rahul"
age = 22

5. What are Python data types?
Main data types:
	•	int
	•	float
	•	str
	•	list
	•	tuple
	•	set
	•	dict
	•	bool

6. Difference between List and Tuple?
List
Tuple
Mutable
Immutable
Uses []
Uses ()
Can modify values
Cannot modify values
Example:

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)


7. What is the difference between == and is?
	•	== compares values
	•	is compares memory locations
Example:

a = [1,2]
b = [1,2]

print(a == b)  # True
print(a is b)  # False


8. What is a function in Python?
A function is a reusable block of code.

def greet():
    print("Hello")

greet()


9. What are arguments and parameters?
	•	Parameters → variables in function definition
	•	Arguments → values passed to function

def add(a, b):   # parameters
    return a + b

add(2, 3)        # arguments


10. What is recursion?
When a function calls itself.
Example:

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))


11. What is a lambda function?
A small anonymous function.

square = lambda x: x * x
print(square(5))


12. What is OOP in Python?
OOP (Object-Oriented Programming) is a programming style based on objects and classes.
Main concepts:
	•	Inheritance
	•	Polymorphism
	•	Encapsulation
	•	Abstraction

13. What is a class and object?
	•	Class → blueprint
	•	Object → real instance of class

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
print(s1.name)


14. What is inheritance?
Inheritance allows one class to use properties of another class.

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass

obj = Child()
obj.show()


15. What is encapsulation?
Wrapping data and methods into one unit (class).
It protects data from direct access.

16. What is polymorphism?
Same function name behaving differently.
Example: + works for numbers and strings.

print(2 + 3)
print("Hello" + " Python")


17. What is exception handling?
Handling runtime errors using:
	•	try
	•	except
	•	finally
Example:

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")


18. What is the difference between syntax error and runtime error?
Syntax Error
Runtime Error
Happens before execution
Happens during execution
Invalid syntax
Logical/runtime issue

19. What is file handling?
Reading and writing files.

file = open("test.txt", "r")
print(file.read())
file.close()


20. What is the use of with open()?
It automatically closes the file.

with open("test.txt", "r") as file:
    print(file.read())


21. What is a module in Python?
A module is a file containing Python code/functions.
Example:
	•	math
	•	random

import math

print(math.sqrt(16))


22. What is list comprehension?
Short way to create lists.

numbers = [x for x in range(5)]
print(numbers)


23. What is the difference between shallow copy and deep copy?
	•	Shallow copy copies references
	•	Deep copy copies complete objects

24. What is self in Python?
self refers to the current object of the class.

25. What is __init__?
Constructor method called automatically when object is created.

class Demo:
    def __init__(self):
        print("Constructor called")

obj = Demo()


#Common Coding Questions with Answers
1. Reverse a String

s = "python"
print(s[::-1])

Output:

nohtyp


2. Check Palindrome

s = "madam"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


3. Find Factorial

num = 5
fact = 1

for i in range(1, num+1):
    fact *= i

print(fact)


4. Fibonacci Series

a, b = 0, 1

for i in range(5):
    print(a)
    a, b = b, a+b


5. Prime Number Check

num = 7

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

#LLM & AI Beginner Interview Questions and Answers
1. What is Artificial Intelligence (AI)?
AI is the field of creating systems that can perform tasks that normally require human intelligence, such as understanding language, recognizing images, making decisions, and solving problems.

2. What is Machine Learning (ML)?
Machine Learning is a subset of AI where systems learn patterns from data instead of being explicitly programmed.
Example:
	•	Spam email detection
	•	Movie recommendations
	•	Fraud detection

3. What is Deep Learning?
Deep Learning is a subset of ML that uses neural networks with many layers to learn complex patterns from large datasets.
Applications:
	•	Chatbots
	•	Image recognition
	•	Speech recognition

4. What is an LLM?
LLM stands for Large Language Model.
An LLM is a deep learning model trained on massive amounts of text data to understand and generate human-like language.
Examples:
	•	OpenAI models like ChatGPT
	•	Google Gemini
	•	Meta Llama

5. How do LLMs work?
LLMs work by:
	1	Reading huge amounts of text
	2	Learning word relationships and patterns
	3	Predicting the next most likely word/token
The core architecture used is usually the Transformer model.

6. What is a Transformer in AI?
A Transformer is a neural network architecture introduced in the paper:
Attention Is All You Need
It uses a mechanism called Attention to understand relationships between words efficiently.

7. What is NLP?
NLP (Natural Language Processing) is a field of AI focused on enabling computers to understand and process human language.
Tasks include:
	•	Translation
	•	Summarization
	•	Sentiment analysis
	•	Chatbots

8. What is a Token in LLMs?
A token is a small piece of text processed by the model.
Example:
	•	“ChatGPT is amazing” may become:
	•	"Chat"
	•	"G"
	•	"PT"
	•	"is"
	•	"amazing"
LLMs process tokens instead of full sentences.

9. What is Training in AI?
Training is the process where a model learns patterns from data by adjusting internal parameters (weights).
More data + compute usually improves performance.

10. What is Fine-Tuning?
Fine-tuning means taking a pretrained model and training it further on domain-specific data.
Example:
	•	Medical chatbot
	•	Legal assistant
	•	Banking support AI






#Database Questions and Answers
1. What is a database?
A database is an organized collection of data that can be easily accessed, managed, and updated.

2. What is DBMS?
DBMS (Database Management System) is software used to create, manage, and manipulate databases.
Examples:
	•	MySQL
	•	Oracle
	•	PostgreSQL
	•	SQL Server

3. What is the difference between DBMS and RDBMS?
DBMS
RDBMS
Stores data as files
Stores data in tables
Less secure
More secure
No relationships
Supports relationships
Example: XML DB
Example: MySQL

4. What is SQL?
SQL (Structured Query Language) is a language used to communicate with relational databases.
Common SQL Commands:
	•	SELECT
	•	INSERT
	•	UPDATE
	•	DELETE
	•	CREATE
	•	DROP

5. What are the types of SQL commands?
Type
Description
DDL
Data Definition Language
DML
Data Manipulation Language
DCL
Data Control Language
TCL
Transaction Control Language
DQL
Data Query Language
Examples:
	•	DDL: CREATE, ALTER, DROP
	•	DML: INSERT, UPDATE, DELETE
	•	DCL: GRANT, REVOKE
	•	TCL: COMMIT, ROLLBACK
	•	DQL: SELECT

6. What is a table?
A table is a collection of rows and columns used to store data in a relational database.

7. What is a primary key?
A primary key uniquely identifies each record in a table.
Properties:
	•	Unique
	•	Cannot contain NULL values
Example:

CREATE TABLE Students (
StudentID INT PRIMARY KEY,
Name VARCHAR(50)
);



8. What is a foreign key?
A foreign key is a field that creates a relationship between two tables.
Example:

CREATE TABLE Orders (
OrderID INT PRIMARY KEY,
StudentID INT,
FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);



9. What is normalization?
Normalization is the process of organizing data to reduce redundancy and improve data integrity.
Normal Forms:
	•	1NF
	•	2NF
	•	3NF
	•	BCNF

10. What is denormalization?
Denormalization is the process of combining tables to improve query performance.

### 8 Problem Solving Questions Solved 

####https://www.geeksforgeeks.org/explore?page=1&category=python&sortBy=submissions&itm_source=geeksforgeeks&itm_medium=main_header&itm_campaign=practice_header


