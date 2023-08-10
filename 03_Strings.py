# Hackerrank.com > Prepare > Python > Strings

# aWAP cASE
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

def swap_case(s):
    new_s = ''
    for char in s:
        if char.islower():
            new_s = new_s + char.upper()
        elif char.isupper():
            new_s = new_s + char.lower()
        else:
            new_s = new_s + char
    return new_s

# Pythonic way to code the same
def swap_case(s):
    return ''.join(char.upper() if char.islower() else char.lower() for char in s)

# Discussion board solution
def swap_case(s)
  return s.swapcase()


##################################################################################################################################################################
# String Split and Join
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:
# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 

def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

##################################################################################################################################################################
# What's Your Name?

def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')


##################################################################################################################################################################
# Mutations
# Read a given string, change the character at a given index and then print the modified string.
# Function Description
# Complete the mutate_string function in the editor below.
# mutate_string has the following parameters:
# string string: the string to change
# int position: the index to insert the character at
# string character: the character to insert
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


##################################################################################################################################################################
# Find a string
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.

def count_substring(string, sub_string):
    # counter will count how many times we have found the substring
    counter = 0
    # position will indicate the position where the substring starts, in case it is found
    position = string.find(sub_string)
    # If the substring was not found on the previous line, position = -1, and it will not enter the while loop
    while position != -1:
        # We found the substring, so we count it
        counter += 1
        # We search again, advancing one place from last position where the substring was found
        position = string.find(sub_string, position + 1)
    return counter

##################################################################################################################################################################
# String Validators
# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    s = input()
    b_alphanumeric = False
    b_alphabetical = False
    b_digits = False
    b_lower = False
    b_upper = False
    
    for char in s:
        # print(char)
        if char.isalnum():
            b_alphanumeric = True
            # print(f'{char} is alphanumeric')
        if char.isalpha():
            b_alphabetical = True
            # print(f'{char} is alphabetical')
        if char.isdigit():
            b_digits = True
            # print(f'{char} is digit')
        if char.islower():
            b_lower = True
            # print(f'{char} is lower case')
        if char.isupper():
            b_upper = True
            # print(f'{char} is upper case')
           
    print(b_alphanumeric)
    print(b_alphabetical)
    print(b_digits)
    print(b_lower)
    print(b_upper)

# Better solution
if __name__ == '__main__':
    inp = input()
    print(any(x.isalnum() for x in inp))
    print(any(x.isalpha() for x in inp))
    print(any(x.isdigit() for x in inp))
    print(any(x.islower() for x in inp))
    print(any(x.isupper() for x in inp))

##################################################################################################################################################################
# Text wrap
# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

import textwrap

def wrap_old(string, max_width):
    new_string = ""
    for counter in range((len(string)//max_width) + 1):
        new_string = new_string + string[counter * max_width: (counter + 1) * max_width] + '\n'
    return new_string

# Using textwrap
def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    

##################################################################################################################################################################
# Designer Door Mat
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# Mat size must be NxM. (N is an odd natural number, and M is N times 3.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

n, m = map(int, (input().split()))
base_pattern = '.|.'
top = ''
bottom = ''
for counter in range(n // 2):
    line = base_pattern * ((counter * 2) + 1)
    dashes = '-' * ((m -1)//2 - (counter * 3) - 1)
    line = dashes + line + dashes + '\n'
    top = top + line
    bottom = line + bottom

dashes = '-' * ((m // 2) - 3)
mat = top + dashes + 'WELCOME' + dashes + '\n' + bottom
print(mat)

# Discussion solution
# input
a, b = map(int, input().split(" "))
# Upper Half
for i in range(1,a,2): print((i*".|.").center(b,"-"))
# Middle
print("WELCOME".center(b,"-"))
# Lower Half
for i in range(a-2,0,-2): print((i*".|.").center(b,"-"))

##################################################################################################################################################################
# String Formatting
# Given an integer, , print the following values for each integer i from 1 to n:
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
def print_formatted(number):
    # calculate the width that will determine the spacing. 2 = 0b10 , so we subtract 2
    width = len(str(bin(n))) - 2
    
    for counter in range(1, number + 1):
        line = str(counter).rjust(width)
        for func in [oct, hex, bin]:
            line += ' ' + str(func(counter))[2:].rjust(width).upper()
        print(line)

# Solution in discussion forum, using f-strings
def print_formatted(num):
    width = len(f"{num:b}")
    for i in range(1, num+1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

    
##################################################################################################################################################################
# Alphabet Rangoli
# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
# size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

def print_rangoli(size):
    # characters sequence
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Select only the characters we will be using, determined by size
    characters = alphabet[:size]
    # Number of characters for the line in the center
    max_width = ((size - 1) * 2 + 1) * 2 - 1  # 4*size-3
    top = ''
    bottom = ''
    for counter in range(1, size + 1):
        # This will go from 'a' to the selected letter, so it is the right half of the string
        right_half = '-'.join(characters[-counter::])
        left_half = right_half[1:][::-1]
        line = (left_half + right_half).center(max_width, '-')
        top += line + '\n'
        # We don't repeat the center line
        if counter < size:
            bottom = line + '\n' + bottom

    rangoli = top + bottom
    print(rangoli)

# Discussion solution
def print_rangoli(size):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,-size,-1):
        temp = '-'.join(alp[size-1:abs(i):-1]+alp[abs(i):size])
        print(temp.center(4*size-3,'-'))

# Most voted solution
import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))

##################################################################################################################################################################


##################################################################################################################################################################
