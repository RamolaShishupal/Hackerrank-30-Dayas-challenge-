#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    dic={}

    a=[]
    

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        # print(firstName)

        emailID = firstNameEmailID[1]
        # print(emailID)
        dic[emailID]=[firstName]
    # print(dic)
    for i in dic:
        # print(i)
        # a=re.findall('\S+@gmail.com',i)
        # e[re.findall('\S+@gmail.com',i)]=dic[i]
        # e.update({a: dic[i]})
        if "@gmail.com" in i:
            a.append(dic[i])
    # print(a)
    a.sort()
    for i in a:
        print(''.join(i))
       
        
       