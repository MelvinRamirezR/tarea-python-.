# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 08:38:17 2021

@author: malvi
"""
lista = [1,2,3,4,5,6,7,8,9,10]

def suma( lista ):
    if len(lista) ==0:
        return 0 
    
    
    return lista.pop(-1) + suma(lista)

print(suma(lista))
