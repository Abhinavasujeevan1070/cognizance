len=[]
a=int(input("Enter the num of records to be stored:"))

for i in range (a):
     e=input("Enter the record (Roll no, Name, Marks):")
     s=e.split()
     f=list(s)
     len.append(f)
print(" no..", "name", "marks", sep='   ')
for i in len:
    print(i[0], i[1], i[2], sep='        ')
m = len[1]
print(m[0], m[1], m[2], sep='   ')