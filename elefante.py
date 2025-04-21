# -*- coding: utf-8 -*-
"""
Created on Tues Jan  7 15:56:10 2025

@author: Raphael Feijó
"""

def incomodam(n):
    i = ("incomodam ")
    if type(n) is not int or n <= 0 :
        return ""

    else:
        n -= 1
        return i + incomodam(n)
    

def elefantes(n, num= - 1):
    num += 1
    if n <= 1:
        return ""
    
    if num == 0:
        return "Um elefante incomoda muita gente\n" + elefantes(n, num)
    
    
    elif num == n + 1:
        return ''
    
    else:      
        if num == 1:
            num = 2
        
        if num == n:
            
            return (str(num) + (" ") + "elefantes" + (" ") + incomodam(num) + "muito mais")
        
        
        else:
            return (str(num)+ (" ") + "elefantes " + incomodam(num) + "muito mais\n" + 
                    str(num) + (" ") + "elefantes incomodam muita gente\n") + elefantes(n, num)
    

    
qtd = int(input("Quantos elefantes incomodam muito a gente?"))
imprimir = elefantes(qtd)
print(imprimir)