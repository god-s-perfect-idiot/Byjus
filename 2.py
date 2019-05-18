'''
# Sample code to perform I/O:

name = input() # Reading input from STDIN
print('Hi, %s.' % name) # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
from collections import Counter
# Write your code here

def split(word):
return [char for char in word]

#def Intersection(lst1, lst2):
# return set(lst1).intersection(lst2)

t = int(input())
for i in range(t):
n=int(input())
x=input()
count = 0
y=input()
x=split(x)
y=split(y)

#z=Intersection(x,y)
c = list((Counter(x) & Counter(y)).elements())
#print(c)
print(len(c))
