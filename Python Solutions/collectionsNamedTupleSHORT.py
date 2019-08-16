from collections import namedtuple
n, nt = int(input()), namedtuple('Student', input().split())
sl = [nt(*input().split()) for i in range(n)]
print('%.2f' % (sum([int(student.MARKS) for student in sl])/n))
