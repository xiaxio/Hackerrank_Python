# Finding the percentage
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
      
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    print(f'{average:.2f}')

# Lists
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    N = int(input())
    commands = list()
    my_list = list()
    for i in range(N):
        command = input()
        
        action = command.split()[0]
        if command == 'print':
            print(my_list)
        elif action == 'insert':
            my_list.insert(int(command.split()[1]), int(command.split()[2]))
        elif action == 'remove':
            my_list.remove(int(command.split()[1]))
        elif action == 'append':
            my_list.append(int(command.split()[1]))
        elif action == 'sort':
            my_list.sort()
        elif action == 'pop':
            my_list.pop()
        elif action == 'reverse':
            my_list.reverse()

# List Comprehension
# You are given three integers  and  representing the dimensions of a cuboid along with an integer . 
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . 
# Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    output = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if (i + j + k) != n]
    print(output)
