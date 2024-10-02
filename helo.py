#!/bin/python3

import math
import os
import random
import re
import sys


__name__ = 'sam'
if __name__ == 'sam':
    n = int(input(""))

    assert n> 1 and n < 101, "n can not be less than 2, not even 1 and n can not be greater than 100"
    
    
    if n % 2  == 1 and n > 1 :
        print ("Weird")
        
        
        

        
    elif n % 2 == 0 :
        if  2<=n<=5:
            print ("Not Weird")
        elif 6<=n<=20:
            print ("Weird")
        elif 21<=n<=100:
            print ("Not Weird")
