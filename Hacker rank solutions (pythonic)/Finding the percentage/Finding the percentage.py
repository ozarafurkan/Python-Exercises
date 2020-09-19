# Problem : https://www.hackerrank.com/challenges/finding-the-percentage/problem
marks={}
for i in range(int(input())):
    name,*mark=input().split()
    mark=list(map(float,mark))
    marks[name]=mark
print("{:.2f}".format( sum(marks[input()])/3 ) )
#print("%.2f"%( sum(marks[input()])/3 ) )
