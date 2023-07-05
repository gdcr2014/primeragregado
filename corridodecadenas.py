# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 22:26:19 2023

@author: Gustavo
"""

cadena = input("escribe una frase:\n")

while cadena != '':
    blancos = 0
    for caracter in cadena:
        if caracter == ' ':
            blancos += 1
       
    palabras = blancos + 1
    print('palabras: ',  palabras)

    cadena = input('escribe una frase: ')    
        
    
    