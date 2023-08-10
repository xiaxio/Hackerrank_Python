#########################################################################################################################################################
# Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")

#########################################################################################################################################################
# Python If-Else
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 6, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

if __name__ == '__main__':
    n = int(input().strip())
    is_odd = n % 2 == 1
    if is_odd:
        print('Weird')
    elif n in range(2, 6) or (n > 20):
        print('Not Weird')
    else:
        print('Weird')

#########################################################################################################################################################
# Arithmetic Operators
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#########################################################################################################################################################
# Python: Division
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division, a // b. 
# The second line should contain the result of float division, a / b.
# No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
  
#########################################################################################################################################################
# Loops
# Task
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i-squared.

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

#########################################################################################################################################################
# Write a function
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

def is_leap(year):
    leap = False
    
    # Verify if year is divisible by 4
    if (year % 4) == 0:
        leap = True
        
    # Check for the exception case
    if ((year % 100) == 0 and (year % 400) != 0):
        leap = False            

    return leap
    
#########################################################################################################################################################
# Print function
# The included code stub will read an integer, n, from STDIN.
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between

if __name__ == '__main__':
    n = int(input())
    m = 0
    for i in range (1, n + 1):
        if i < 10:
            m = m * 10 + i
        elif i < 100:
            m = m * 100 + i
        elif i < 1000:
            m = m * 1000 + i
    print(m)
    
#########################################################################################################################################################

