# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 08:48:10 2021

@author: malvi
"""

lista = [1,2,3,4,5,6,7,8,9,10,11]

def medio(lista):
    if len(lista)%2 ==0:
        if len( lista ) ==2:
            lista.pop(1)
            
            return lista 
        lista.pop(0)
        lista.pop
        
        return medio(lista)
    
    if len( lista ) ==1:
        return lista 
    lista.pop(0)
    lista.pop(-1)
    
    return medio(lista)