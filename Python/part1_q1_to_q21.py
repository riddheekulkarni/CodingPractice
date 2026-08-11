# =============================================================
# PYTHON PRACTICAL EXAM - QUESTIONS 1 to 21
# (Second set of 21 questions from assignment)
# =============================================================


# =============================================================
# Q1. Write a Python program to input a string and:
#     - Create a function to count vowels and consonants.
#     - Display the result in proper format.
# =============================================================

def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for ch in s:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

s = input("Q1 - Enter a string: ")
v, c = count_vowels_consonants(s)
print(f"Vowels    : {v}")
print(f"Consonants: {c}")


# =============================================================
# Q2. Write a program to:
#     - Input a number.
#     - Create a function to check palindrome.
#     - Convert the number to string and verify using string slicing.
# =============================================================

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

num = int(input("\nQ2 - Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is NOT a Palindrome")


# =============================================================
# Q3. Write a program to:
#     - Input a sentence.
#     - Count number of words using string operations.
#     - Use a function to return the longest word.
# =============================================================

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

sentence = input("\nQ3 - Enter a sentence: ")
words = sentence.split()
print(f"Number of words: {len(words)}")
print(f"Longest word   : {longest_word(sentence)}")


# =============================================================
# Q4. Write a program to:
#     - Generate Fibonacci series up to n terms using loop.
#     - Create a function to check if a number in series is even or odd.
# =============================================================

def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

n = int(input("\nQ4 - Enter number of terms for Fibonacci: "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
    print(f"  {a} -> {check_even_odd(a)}")
    a, b = b, a + b


# =============================================================
# Q5. Write a program to:
#     - Input a number.
#     - Use loop to calculate factorial.
#     - Create a function to check if result is divisible by 5.
# =============================================================

def divisible_by_5(n):
    return n % 5 == 0

num = int(input("\nQ5 - Enter a number to find factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} = {fact}")
if divisible_by_5(fact):
    print(f"{fact} IS divisible by 5")
else:
    print(f"{fact} is NOT divisible by 5")


# =============================================================
# Q6. Write a program to:
#     - Print multiplication table of a number.
#     - Use a function to check whether each result is prime.
# =============================================================

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("\nQ6 - Enter a number for multiplication table: "))
print(f"Multiplication Table of {num}:")
for i in range(1, 11):
    result = num * i
    prime_status = "Prime" if is_prime(result) else "Not Prime"
    print(f"  {num} x {i:2} = {result:4}  ({prime_status})")


# =============================================================
# Q7. Write a program to:
#     - Input a string.
#     - Use loop to count frequency of each character.
#     - Create a function to display highest occurring character.
# =============================================================

def highest_occurring(freq):
    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]

s = input("\nQ7 - Enter a string: ")
freq = {}
for ch in s:
    if ch != ' ':
        freq[ch] = freq.get(ch, 0) + 1

print("Character Frequencies:")
for ch, count in freq.items():
    print(f"  '{ch}' : {count}")

max_char, max_count = highest_occurring(freq)
print(f"Highest occurring character: '{max_char}' ({max_count} times)")


# =============================================================
# Q8. Write a program to:
#     - Reverse a string using loop.
#     - Create a function to check whether reversed string
#       is same as original.
# =============================================================

def is_same(original, reversed_str):
    return original == reversed_str

s = input("\nQ8 - Enter a string: ")
reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s

print(f"Original : {s}")
print(f"Reversed : {reversed_s}")
if is_same(s, reversed_s):
    print("Both are the SAME (Palindrome)")
else:
    print("Both are DIFFERENT (Not a Palindrome)")


# =============================================================
# Q9. Write a program to:
#     - Input two strings.
#     - Use a function to check whether they are anagrams.
#     - Display result.
# =============================================================

def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

s1 = input("\nQ9 - Enter first string : ")
s2 = input("Q9 - Enter second string: ")
if are_anagrams(s1, s2):
    print(f"'{s1}' and '{s2}' ARE Anagrams")
else:
    print(f"'{s1}' and '{s2}' are NOT Anagrams")


# =============================================================
# Q10. Write a program to:
#      - Input a paragraph.
#      - Use regex to extract all email IDs.
#      - Create a function to count total valid emails.
# =============================================================

import re

def count_emails(email_list):
    return len(email_list)

paragraph = input("\nQ10 - Enter a paragraph (with email IDs): ")
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', paragraph)
print("Emails found:", emails)
print("Total valid emails:", count_emails(emails))


# =============================================================
# Q11. Write a program to:
#      - Input a string.
#      - Use regex to replace multiple spaces with a single space.
#      - Create a function to count words.
# =============================================================

def count_words(s):
    return len(s.split())

s = input("\nQ11 - Enter a string (with extra spaces): ")
cleaned = re.sub(r' +', ' ', s).strip()
print(f"Original : '{s}'")
print(f"Cleaned  : '{cleaned}'")
print(f"Word count: {count_words(cleaned)}")


# =============================================================
# Q12. Write a program to:
#      - Validate password using regex (length, digit, special char).
#      - Create a function to display strength (Weak/Medium/Strong).
# =============================================================

def password_strength(password):
    has_length  = len(password) >= 8
    has_digit   = bool(re.search(r'\d', password))
    has_upper   = bool(re.search(r'[A-Z]', password))
    has_special = bool(re.search(r'[!@#$%^&*]', password))

    score = sum([has_length, has_digit, has_upper, has_special])

    if score <= 1:
        return "Weak"
    elif score <= 3:
        return "Medium"
    else:
        return "Strong"

password = input("\nQ12 - Enter a password: ")
strength = password_strength(password)
print(f"Password Strength: {strength}")


# =============================================================
# Q13. Write a program to:
#      - Read a file.
#      - Count number of words and lines.
#      - Create a function to find longest word.
# =============================================================

def find_longest_word(content):
    words = content.split()
    return max(words, key=len) if words else "No words found"

# Create a sample file first
with open("sample.txt", "w") as f:
    f.write("Python is a powerful programming language.\n")
    f.write("It is easy to learn and use.\n")
    f.write("Python supports object oriented programming.\n")

with open("sample.txt", "r") as f:
    content = f.read()

lines = content.strip().split('\n')
words = content.split()
print("\nQ13 - File Reading:")
print(f"Number of lines: {len(lines)}")
print(f"Number of words: {len(words)}")
print(f"Longest word   : {find_longest_word(content)}")


# =============================================================
# Q14. Write a program to:
#      - Write user input into a file.
#      - Read file and count frequency of specific word.
#      - Display the frequency of word using function.
# =============================================================

def count_word_frequency(filename, word):
    with open(filename, "r") as f:
        content = f.read().lower()
    return content.split().count(word.lower())

print("\nQ14 - Write to File:")
text = input("Enter text to write to file: ")
with open("user_file.txt", "w") as f:
    f.write(text)
print("Text written to user_file.txt")

word = input("Enter word to search: ")
freq = count_word_frequency("user_file.txt", word)
print(f"'{word}' appears {freq} time(s) in the file")


# =============================================================
# Q15. Write a program to:
#      - Copy contents of one file to another.
#      - Create a function to count characters in new file.
# =============================================================

def count_characters(filename):
    with open(filename, "r") as f:
        return len(f.read())

with open("source.txt", "w") as f:
    f.write("This is the source file.\nIt has some content.")

with open("source.txt", "r") as f:
    data = f.read()
with open("destination.txt", "w") as f:
    f.write(data)

print("\nQ15 - File Copy:")
print("Contents copied from source.txt to destination.txt")
print(f"Character count in new file: {count_characters('destination.txt')}")


# =============================================================
# Q16. Write a program to:
#      - Read a file containing mixed data.
#      - Use regex to extract all numbers.
#      - Create a function to find their sum.
# =============================================================

def sum_of_numbers(num_list):
    return sum(num_list)

with open("mixed.txt", "w") as f:
    f.write("I have 3 cats and 12 fish. My age is 20 and I have 5 bags.")

with open("mixed.txt", "r") as f:
    content = f.read()

numbers = list(map(int, re.findall(r'\d+', content)))
print("\nQ16 - Extract Numbers from File:")
print(f"Content  : {content}")
print(f"Numbers  : {numbers}")
print(f"Sum      : {sum_of_numbers(numbers)}")


# =============================================================
# Q17. Write a program to:
#      - Read a file with email IDs.
#      - Validate using regex.
#      - Store valid emails in another file.
# =============================================================

with open("emails.txt", "w") as f:
    f.write("alice@gmail.com\nbob@yahoo.com\ninvalid-email\ntest@.com\ncarol@college.edu")

with open("emails.txt", "r") as f:
    all_emails = f.read().splitlines()

valid = [e for e in all_emails if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', e)]

with open("valid_emails.txt", "w") as f:
    f.write("\n".join(valid))

print("\nQ17 - Email Validation:")
print("All emails  :", all_emails)
print("Valid emails:", valid)
print("Valid emails saved to valid_emails.txt")


# =============================================================
# Q18. Write a program to:
#      - Read file content.
#      - Replace all digits with '*' using regex.
#      - Count replacements using function.
# =============================================================

def count_replacements(original, pattern):
    return len(re.findall(pattern, original))

with open("digits.txt", "w") as f:
    f.write("Phone: 9876543210, Pin: 1234, Age: 21")

with open("digits.txt", "r") as f:
    content = f.read()

count = count_replacements(content, r'\d')
replaced = re.sub(r'\d', '*', content)

print("\nQ18 - Replace Digits:")
print(f"Original    : {content}")
print(f"After replace: {replaced}")
print(f"Total digits replaced: {count}")


# =============================================================
# Q19. Write a program to:
#      - Input a string.
#      - Check whether it is palindrome ignoring spaces.
#      - Use function for validation.
# =============================================================

def is_palindrome_ignore_spaces(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

s = input("\nQ19 - Enter a string: ")
if is_palindrome_ignore_spaces(s):
    print(f"'{s}' IS a palindrome (ignoring spaces)")
else:
    print(f"'{s}' is NOT a palindrome (ignoring spaces)")


# =============================================================
# Q20. Write a program to:
#      - Input marks of students.
#      - Assign grades using control statements.
#      - Store results in a list and display using function.
# =============================================================

def display_results(results):
    print("Student Results:")
    for name, marks, grade in results:
        print(f"  {name:10} | Marks: {marks} | Grade: {grade}")

def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'

n = int(input("\nQ20 - How many students? "))
results = []
for i in range(n):
    name  = input(f"  Enter name of student {i+1}: ")
    marks = int(input(f"  Enter marks of {name}: "))
    grade = assign_grade(marks)
    results.append((name, marks, grade))

display_results(results)


# =============================================================
# Q21. Write a program to:
#      - Generate factorials of numbers from 1 to n.
#      - Store results in file.
#      - Create function to retrieve highest factorial.
# =============================================================

def get_highest_factorial(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    last_line = lines[-1].strip()
    return last_line

n = int(input("\nQ21 - Enter n to generate factorials from 1 to n: "))
fact = 1
with open("factorials.txt", "w") as f:
    for i in range(1, n + 1):
        fact *= i
        f.write(f"{i}! = {fact}\n")
        print(f"  {i}! = {fact}")

print(f"All factorials saved to factorials.txt")
print(f"Highest factorial: {get_highest_factorial('factorials.txt')}")
