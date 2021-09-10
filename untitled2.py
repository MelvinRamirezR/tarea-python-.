# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 08:53:53 2021

@author: malvi
"""

def printRev (n):
    if n>=0 :
        print(n)
        if n ==0:
            print("BOOOMMM!!!")
            return
        printRev(n-1)
        
        n=10
        printRev(n) 
        
            