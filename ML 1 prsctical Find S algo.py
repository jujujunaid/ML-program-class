#Implementation of find S algorithm
import csv
a=[]
with  open('D:\practice\enjoysports.csv','r') as csvfile:
    for row in csv.reader(csvfile):
        a.append(row)
        print("\n",a)
print("The total no. of traning instance are :",len(a)-1)
na = len(a[0])-1
print("The total no of num attribute are :",len(a[0])-1)
print("Initial hypo : ")
hypo = ['0']*na
print(hypo)
for i in range(len(a)):
    if a[i][na]=='yes':
        for j in range(na):
            if hypo[j]=='0' or hypo[j]==a[i][j]:
                hypo[j]=a[i][j]
            else:
                hypo[j]='?'
                print(hypo)
print("\n hypo {} is :\n".format(i),hypo)
print("\n the specific hypo is")
print(hypo)