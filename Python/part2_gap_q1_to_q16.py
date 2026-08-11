# =============================================================
# PYTHON PRACTICAL EXAM - GAP QUESTIONS 1 to 16
# (Topics missing from 47 questions, added from syllabus)
# =============================================================


# =============================================================
# GAP Q1. Write a Python program to:
#         - Input a list of numbers from the user.
#         - Store them in a tuple.
#         - Perform slicing to display first half and second half.
#         - Demonstrate packing and unpacking of tuple values.
# =============================================================

print("GAP Q1 - Tuples: Slicing, Packing, Unpacking")
print("=" * 50)

n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

my_tuple = tuple(numbers)
print("Tuple:", my_tuple)

mid = len(my_tuple) // 2
print("First Half :", my_tuple[:mid])
print("Second Half:", my_tuple[mid:])

# Packing - bundling values into a tuple
packed = my_tuple[0], my_tuple[1], my_tuple[2]
print("Packed (first 3 values):", packed)

# Unpacking - pulling values out of tuple into variables
a, b, c = packed
print(f"Unpacked -> a={a}, b={b}, c={c}")


# =============================================================
# GAP Q2. Write a Python program to:
#         - Accept two tuples from the user.
#         - Compare them and display which is greater.
#         - Convert both tuples to lists, merge and sort them,
#           then convert back to tuple and display.
# =============================================================

print("\nGAP Q2 - Tuples: Compare, Merge and Sort")
print("=" * 50)

t1 = tuple(int(x) for x in input("Enter first tuple values (space separated): ").split())
t2 = tuple(int(x) for x in input("Enter second tuple values (space separated): ").split())

print("Tuple 1:", t1)
print("Tuple 2:", t2)

if t1 > t2:
    print("Tuple 1 is greater")
elif t1 < t2:
    print("Tuple 2 is greater")
else:
    print("Both tuples are equal")

list1 = list(t1)
list2 = list(t2)
merged = list1 + list2
merged.sort()
result = tuple(merged)
print("Merged and Sorted Tuple:", result)


# =============================================================
# GAP Q3. Write a Python program to:
#         - Accept two sets of numbers from the user.
#         - Use a function to perform and display union,
#           intersection, difference, and symmetric difference
#           of the two sets.
# =============================================================

print("\nGAP Q3 - Sets: All Set Operations")
print("=" * 50)

def set_operations(s1, s2):
    print("Union                :", s1 | s2)
    print("Intersection         :", s1 & s2)
    print("Difference (S1 - S2) :", s1 - s2)
    print("Symmetric Difference :", s1 ^ s2)

set1 = set(int(x) for x in input("Enter first set (space separated): ").split())
set2 = set(int(x) for x in input("Enter second set (space separated): ").split())

print("Set 1:", set1)
print("Set 2:", set2)
set_operations(set1, set2)


# =============================================================
# GAP Q4. Write a Python program to:
#         - Input a sentence from the user.
#         - Convert it into a set of unique words.
#         - Use a function to check if one set of words is a
#           subset of another.
#         - Also demonstrate frozenset.
# =============================================================

print("\nGAP Q4 - Sets: Unique Words, Subset Check, Frozenset")
print("=" * 50)

def check_subset(s1, s2):
    if s1.issubset(s2):
        print("Sentence 1 words ARE a subset of sentence 2 words")
    elif s2.issubset(s1):
        print("Sentence 2 words ARE a subset of sentence 1 words")
    else:
        print("Neither sentence is a subset of the other")

sentence1 = input("Enter first sentence : ")
sentence2 = input("Enter second sentence: ")

words1 = set(sentence1.lower().split())
words2 = set(sentence2.lower().split())

print("Unique words in sentence 1:", words1)
print("Unique words in sentence 2:", words2)

check_subset(words1, words2)

frozen = frozenset(words1)
print("Frozenset:", frozen)
print("(Frozenset is immutable - elements cannot be added or removed)")


# =============================================================
# GAP Q5. Write a Python program to:
#         - Create a dictionary of student names and their marks.
#         - Use a function to display the student with the
#           highest marks (topper).
#         - Allow the user to add a new student and delete
#           an existing one.
# =============================================================

print("\nGAP Q5 - Dictionary: Student Marks, Topper, Add, Delete")
print("=" * 50)

def find_topper(d):
    topper = max(d, key=d.get)
    print(f"Topper: {topper} with {d[topper]} marks")

n = int(input("How many students? "))
students = {}
for i in range(n):
    name  = input(f"  Enter name of student {i+1}: ")
    marks = int(input(f"  Enter marks of {name}: "))
    students[name] = marks

print("Students:", students)
find_topper(students)

new_name  = input("Enter new student name to add: ")
new_marks = int(input(f"Enter marks of {new_name}: "))
students[new_name] = new_marks
print("After adding:", students)

del_name = input("Enter student name to delete: ")
if del_name in students:
    del students[del_name]
    print(f"'{del_name}' deleted.")
else:
    print("Student not found.")
print("Final Dictionary:", students)


# =============================================================
# GAP Q6. Write a Python program to:
#         - Input a sentence from the user.
#         - Count frequency of each word using a dictionary.
#         - Use a function to display the most repeated word
#           and its count.
# =============================================================

print("\nGAP Q6 - Dictionary: Word Frequency Counter")
print("=" * 50)

def most_repeated(d):
    word = max(d, key=d.get)
    print(f"Most repeated word: '{word}' (appears {d[word]} times)")

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Word Frequencies:", freq)
most_repeated(freq)


# =============================================================
# GAP Q7. Write a Python program to:
#         - Create two dictionaries representing monthly
#           expenses for two people.
#         - Merge them.
#         - Use dictionary comprehension to create a new
#           dictionary showing the difference in their
#           expenses for each month.
# =============================================================

print("\nGAP Q7 - Dictionary: Merge and Comprehension")
print("=" * 50)

person1 = {"Jan": 3000, "Feb": 4000, "Mar": 3500}
person2 = {"Jan": 2500, "Feb": 4200, "Mar": 3000}

print("Person 1 expenses:", person1)
print("Person 2 expenses:", person2)

merged = {**person1, **person2}
print("Merged dictionary:", merged)

difference = {month: abs(person1[month] - person2[month]) for month in person1}
print("Expense difference per month:", difference)


# =============================================================
# GAP Q8. Write a Python program to:
#         - Input a list of numbers from the user.
#         - Use lambda with map() to square each number.
#         - Use lambda with filter() to keep only even numbers.
#         - Use lambda with reduce() to find product of the list.
#         - Display all results.
# =============================================================

from functools import reduce

print("\nGAP Q8 - Lambda with map(), filter(), reduce()")
print("=" * 50)

numbers = list(map(int, input("Enter numbers (space separated): ").split()))
print("Original list      :", numbers)

squared = list(map(lambda x: x**2, numbers))
print("Squared (map)      :", squared)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers (filter)   :", evens)

product = reduce(lambda x, y: x * y, numbers)
print("Product of all (reduce) :", product)


# =============================================================
# GAP Q9. Write a Python program to:
#         - Create a class Student with attributes name,
#           roll number, and marks.
#         - Use __init__ to initialise and __del__ to display
#           a message when object is deleted.
#         - Create a class method to display grade based on marks.
#         - Create two objects and demonstrate.
# =============================================================

print("\nGAP Q9 - OOP: Student Class with __init__ and __del__")
print("=" * 50)

class Student:
    def __init__(self, name, roll, marks):
        self.name  = name
        self.roll  = roll
        self.marks = marks
        print(f"Object created for student: {self.name}")

    def display_grade(self):
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 75:
            grade = "B"
        elif self.marks >= 60:
            grade = "C"
        elif self.marks >= 40:
            grade = "D"
        else:
            grade = "F"
        print(f"Name: {self.name} | Roll: {self.roll} | Marks: {self.marks} | Grade: {grade}")

    def __del__(self):
        print(f"Object deleted for student: {self.name}")

s1 = Student("Alice", 101, 88)
s2 = Student("Bob",   102, 45)

s1.display_grade()
s2.display_grade()

del s1
del s2


# =============================================================
# GAP Q10. Write a Python program to:
#          - Create a base class Shape with a method area().
#          - Create derived classes Circle and Rectangle
#            that override the area() method.
#          - Use a function to accept user choice and display
#            the area of the selected shape.
# =============================================================

import math

print("\nGAP Q10 - Inheritance: Shape, Circle, Rectangle")
print("=" * 50)

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(math.pi * self.radius ** 2, 2)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length  = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

def display_area(choice):
    if choice == 1:
        r   = float(input("Enter radius: "))
        obj = Circle(r)
        print(f"Area of Circle    : {obj.area()}")
    elif choice == 2:
        l   = float(input("Enter length: "))
        b   = float(input("Enter breadth: "))
        obj = Rectangle(l, b)
        print(f"Area of Rectangle : {obj.area()}")
    else:
        print("Invalid choice")

print("1. Circle")
print("2. Rectangle")
ch = int(input("Enter choice: "))
display_area(ch)


# =============================================================
# GAP Q11. Write a Python program to:
#          - Create a class Fraction with numerator and
#            denominator.
#          - Overload the + operator to add two fractions.
#          - Overload the == operator to check if two fractions
#            are equal.
#          - Display result using __str__.
# =============================================================

print("\nGAP Q11 - Operator Overloading: Fraction Class")
print("=" * 50)

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den

    def __str__(self):
        return f"{self.num}/{self.den}"

n1, d1 = map(int, input("Enter first fraction  (numerator denominator): ").split())
n2, d2 = map(int, input("Enter second fraction (numerator denominator): ").split())

f1 = Fraction(n1, d1)
f2 = Fraction(n2, d2)

print(f"Fraction 1 : {f1}")
print(f"Fraction 2 : {f2}")
print(f"Sum        : {f1 + f2}")
print(f"Equal?     : {f1 == f2}")


# =============================================================
# GAP Q12. Write a Python program to:
#          - Input a list of numbers from the user using a loop.
#          - Use pass to skip negative numbers without doing anything.
#          - Use a while-else loop to search for a specific number
#            and display whether it was found or not.
# =============================================================

print("\nGAP Q12 - pass Statement and while...else Loop")
print("=" * 50)

numbers = list(map(int, input("Enter numbers (space separated): ").split()))

print("Positive numbers (skipping negatives using pass):")
for num in numbers:
    if num < 0:
        pass           # do nothing for negative numbers
    else:
        print(num, end=" ")
print()

target = int(input("Enter a number to search: "))
i = 0
while i < len(numbers):
    if numbers[i] == target:
        print(f"{target} found at index {i}")
        break
    i += 1
else:
    print(f"{target} was NOT found in the list")


# =============================================================
# GAP Q13. Write a Python program to:
#          - Write some text into a file.
#          - Use tell() to display cursor position after writing.
#          - Use seek(0) to move back to the beginning and read.
#          - Use seek() with a specific offset to read from
#            the middle of the file.
# =============================================================

print("\nGAP Q13 - File: tell() and seek()")
print("=" * 50)

with open("cursor_demo.txt", "w") as f:
    f.write("Hello World! Python is great.")

f = open("cursor_demo.txt", "r")

print("Cursor at start         :", f.tell())

data = f.read(5)
print(f"Read 5 characters       : '{data}'")
print("Cursor after reading 5  :", f.tell())

f.seek(0)
print("After seek(0), cursor   :", f.tell())
print("Full content            :", f.read())

f.seek(13)
print("After seek(13), reading :", f.read())

f.close()


# =============================================================
# GAP Q14. Write a Python program to:
#          - Create a file and write data into it.
#          - Rename the file using os.rename().
#          - List all files in the current directory using
#            os.listdir().
#          - Delete the renamed file using os.remove().
# =============================================================

import os

print("\nGAP Q14 - File: Rename, List Directory, Delete")
print("=" * 50)

with open("old_name.txt", "w") as f:
    f.write("This file will be renamed and then deleted.")
print("File created : old_name.txt")

os.rename("old_name.txt", "new_name.txt")
print("File renamed : old_name.txt -> new_name.txt")

print("Files in current directory:")
for filename in os.listdir("."):
    print("  -", filename)

os.remove("new_name.txt")
print("File deleted : new_name.txt")


# =============================================================
# GAP Q15. Write a Python program to:
#          - Input a string from the user.
#          - Use ord() to display ASCII value of each character.
#          - Use chr() to convert a list of ASCII values back
#            to a string.
#          - Use maketrans() and translate() to create a simple
#            cipher that shifts each letter by 1.
# =============================================================

print("\nGAP Q15 - Strings: ord(), chr(), maketrans(), translate()")
print("=" * 50)

text = input("Enter a string: ")

print("ASCII values using ord():")
for ch in text:
    print(f"  '{ch}' -> {ord(ch)}")

ascii_list = [72, 101, 108, 108, 111]
converted  = "".join(chr(x) for x in ascii_list)
print(f"chr() on {ascii_list} -> '{converted}'")

table  = str.maketrans("abcdefghijklmnopqrstuvwxyz",
                        "bcdefghijklmnopqrstuvwxyza")
cipher = text.lower().translate(table)
print(f"Original string  : {text}")
print(f"Encrypted string : {cipher}")


# =============================================================
# GAP Q16. Write a Python program to:
#          - Create a function using *args to accept any number
#            of numbers and return their sum and average.
#          - Create another function using **kwargs to accept
#            student details (name, age, grade) and display
#            them in a formatted way.
# =============================================================

print("\nGAP Q16 - *args and **kwargs")
print("=" * 50)

def calculate(*args):
    total = sum(args)
    avg   = total / len(args)
    print(f"Numbers entered : {args}")
    print(f"Sum             : {total}")
    print(f"Average         : {avg:.2f}")

def display_student(**kwargs):
    print("Student Details:")
    for key, value in kwargs.items():
        print(f"  {key:10}: {value}")

numbers = list(map(int, input("Enter numbers for *args demo (space separated): ").split()))
calculate(*numbers)

print()
display_student(name="Alice", age=20, grade="A", city="Pune")
