import math
import os
import random
import re
import sys

n= int(input(""))

while n<=100 and 1<=n:
    a = n % 2
    if (a!=0):
        print("Weird")
        break
    elif (2<=n<=5 and n!=3):
        print("Not Weird")
        break
    elif (6<=n<=20):
        print("Weird")
        break
    else:
        print("Not Weird") 
        break
