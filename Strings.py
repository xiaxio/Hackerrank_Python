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
