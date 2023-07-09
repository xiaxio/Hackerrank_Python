# Python Evaluation
# You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).
text = input()
# print(eval(text.split('(')[1].split(')')[0]))
a = eval(text)
# did not accept print(eval(text)) (it prints an extra line), but just doing a = eval(text), it passes the challenge
# Discussions answer: eval(input())
