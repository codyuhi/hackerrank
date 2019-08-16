# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
student = namedtuple('student','ID MARKS NAME CLASS')
number_of_students = int(input())
#print(number_of_students)
#print(input())
student_list = []
columns = list(map(str,input().split()))
student_id = int()
student_marks = int()
student_name = int()
student_class = int()
for i in range(4):
    if columns[i] == "ID":
        student_id = i
    elif columns[i] == "MARKS":
        student_marks = i
    elif columns[i] == "NAME":
        student_name = i
    elif columns[i] == "CLASS":
        student_class = i
for i in range(number_of_students):
    #print(i)
    new_column = list(map(str,input().split()))
    new_student = student(new_column[student_id],new_column[student_marks],new_column[student_name],new_column[student_class])
    #print(new_student)
    student_list.append(new_student)
#print(student_list)
avg_marks = float(0)
for i in range(len(student_list)):
    avg_marks += float(student_list[i].MARKS)
avg_marks /= float(number_of_students)
print("{0:.2f}".format(round(avg_marks, 2)))
