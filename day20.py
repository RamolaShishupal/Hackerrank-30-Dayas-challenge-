#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
# print(a)
c=0
s=0
for i in range(len(a)):
    
    for j in range(i):
        if a[j]>a[i]:
            s=a[j]+a[i]
            a[j]=s-a[j]
            a[i]=s-a[j]
            
            c=c+1
        # print(a[j],a[i])


        
  
   
    
print('Array is sorted in', c ,'swaps.')
print('First Element:',a[0])
print('Last Element:',a[-1])
