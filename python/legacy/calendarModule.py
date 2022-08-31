# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
given = list(map(int,input().split()))
month = given[0]
day = given[1]
year = given[2]
print(calendar.day_name[calendar.weekday(year, month, day)].upper())
