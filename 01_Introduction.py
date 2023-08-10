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


#########################################################################################################################################################


#########################################################################################################################################################


#########################################################################################################################################################

