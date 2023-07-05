# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:45:07 2023

@author: Gustavo
"""
from turtle import Screen, Turtle

#califiaciones
suspensos = int(input("indique la cantidad de suspensos"))
aprobados = int(input("indique la cantidad de aprobados"))
notables = int(input("indique la cantidad de notables"))
sobresalientes = int(input("indique la cantidad de sobresalientes"))

#radio del circulo
radio = 300

#pantalla
pantalla = Screen()
tortuga = Turtle()
tortuga.speed(0)

#dibujo del circulo
tortuga .penup()
tortuga.goto(0, -radio)
tortuga.pendown()
tortuga.circle(radio)
tortuga.penup()
tortuga.home()
tortuga.pendown()

#dibujo de lineas de los suspensos
angulo = 360 * suspensos / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)
#escribir el texto para los suspensos
tortuga.penup()
tortuga.right(angulo/2)
tortuga.forward(radio/2)
tortuga.write("suspensos")
tortuga.backward(radio/2)
tortuga.left(angulo/2)
tortuga.pendown() 

#dibujo de linea para los aprobados
angulo = 360 * aprobados / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#escriir el texto de aprobados
tortuga.penup()
tortuga.right(angulo/2)
tortuga.forward(radio/2)
tortuga.write("aprobados")
tortuga.backward(radio/2)
tortuga.left(angulo/2)
tortuga.pendown() 

#dibujo de linea para los notables
angulo = 360 * aprobados / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#escriir el texto de notables
tortuga.penup()
tortuga.right(angulo/2)
tortuga.forward(radio/2)
tortuga.write("notables")
tortuga.backward(radio/2)
tortuga.left(angulo/2)
tortuga.pendown() 

#dibujo de linea para los sobresalientes
angulo = 360 * aprobados / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#escriir el texto de sobresalientes
tortuga.penup()
tortuga.right(angulo/2)
tortuga.forward(radio/2)
tortuga.write("sobresalientes")
tortuga.backward(radio/2)
tortuga.left(angulo/2)
tortuga.hideturtle()
tortuga.pendown() 
tortuga.hideturtle()



#salir del sistema
pantalla.exitonclick()
