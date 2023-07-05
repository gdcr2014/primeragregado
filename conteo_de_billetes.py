# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:36:21 2023

@author: Gustavo
"""
dinero = int(input("ingrese una cantidad de dinero a desglosar: "))

billetes500 = dinero // 500
billetes200 = (dinero % 500) // 200
billetes100 = ((dinero % 500) % 200) // 100
billetes50 = (((dinero % 500) % 200) % 100) // 50
billetes20 = ((((dinero % 500) % 200) % 100) % 50) // 20
billetes10 = (((((dinero % 500) % 200) % 100) % 50) % 20) // 10
billetes5 = ((((((dinero % 500) % 200) % 100) % 50) % 20) % 10) // 5
billetes2 = (((((((dinero % 500) % 200) % 100) % 50) % 20) % 10) % 5) // 2
billetes1 = ((((((((dinero % 500) % 200) % 100) % 50) % 20) % 10) % 5) % 2) // 1

if dinero >=1:
    print("500: ",billetes500)
    print("200: ",billetes200)
    print("100: ",billetes100)
    print("50: ",billetes50)
    print("20: ",billetes20)
    print("10: ",billetes10)
    print("5: ",billetes5)
    print("2: ",billetes2)
    print("1: ",billetes1)
    
if dinero <= 0:
    print("ingrese un valor positivo")