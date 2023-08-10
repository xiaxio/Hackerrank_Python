#########################################################################################################################################################
# List Comprehension
# You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
# Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. 
# Here, 0<=i<=x; 0<=j<=y; 0<=k<=z. Please use list comprehensions rather than multiple loops, as a learning exercise.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    output = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range (z+1) if (i + j + k) != n]
    print(output)


#########################################################################################################################################################
# Find the Runner-Up Score!
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given  scores. Store them in a list and find the score of the runner-up.
# The first line contains n. The second line contains an array A[]  of n integers each separated by a space.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    my_list = list(arr)
    max_n = max(my_list)
    runner_up = [x for x in my_list if x < max_n]
    print(max(runner_up))

# Solution in Discussion board:
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
		
    runnerup = sorted(set(arr), reverse=True)[1]
    print(runnerup)


#########################################################################################################################################################
# Nested lists
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) 
# having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    # lists initialization
    names = list()
    grades = list()
    
    # Collect data  from STDIN
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # Store input in lists
        names.append(name)
        grades.append(score)
        
    # Find second lowest grade. sorted() returns a list object
    second_lowest = sorted(set(grades))[1]
    
    # Find the indexes in grades that match the second lowest grade
    names_indexes = [i for i in range(len(grades)) if grades[i] == second_lowest]
    # Create list to save the names of the students who scored the second lowest grade
    students_with_second_lowest_grade = list()
    # Populate the list
    for i in names_indexes:
        students_with_second_lowest_grade.append(names[i])
    # Sort the students list alphabetically    
    students_with_second_lowest_grade.sort()
    # Print the students names
    for i in students_with_second_lowest_grade:
        print(i)    


#########################################################################################################################################################
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


#########################################################################################################################################################
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


#########################################################################################################################################################
# Tuples
# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))



