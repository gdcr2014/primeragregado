# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:50:26 2023

@author: Gustavo
"""
from turtle import Screen, Turtle
from math import sqrt

pantalla = Screen()
pantalla.setup(1025,1025)
pantalla.screensize(1000,1000)
pantalla.setworldcoordinates(-500,-500,500,500)
pantalla.delay(0)


x1 = 100
y1 = 200
velocidad_x1 = 0.1
velocidad_y1 = 0
m1 = 20

x2 = -100
y2 = -200
velocidad_x2 = -0.1
velocidad_y2 = 0
m2 = 20

x3 = -200
y3 = -200
velocidad_x3 = 0.1
velocidad_y3 = 0
m3 = 20

x4 = 200
y4 = 200
velocidad_x4 = -0.1
velocidad_y4 = 0
m4 = 20

cuerpo1 = Turtle('circle')
cuerpo1.color('red')
cuerpo1.speed(0)
cuerpo1.penup()
cuerpo1.goto(x1,y1)
cuerpo1.pendown()

cuerpo2 = Turtle('circle')
cuerpo2.color('blue')
cuerpo2.speed(0)
cuerpo2.penup()
cuerpo2.goto(x2,y2)
cuerpo2.pendown()

cuerpo3 = Turtle('circle')
cuerpo3.color('green')
cuerpo3.speed(0)
cuerpo3.penup()
cuerpo3.goto(x2,y1)
cuerpo3.pendown()

cuerpo4 = Turtle('circle')
cuerpo4.color('yellow')
cuerpo4.speed(0)
cuerpo4.penup()
cuerpo4.goto(x1,y1)
cuerpo4.pendown()

for t in range(10000):
    r = sqrt( (x2-x1)**2 + (y2-y1)**2)
    vc = r ** 3

    aceleracion_x1 = m2 * (x2-x1) / vc
    aceleracion_y1 = m2 * (y2-y1) / vc
    aceleracion_x2 = m1 * (x1-x2) / vc
    aceleracion_y2 = m1 * (y1-y2) / vc
    aceleracion_x3 = m4 * (x4-x3) / vc
    aceleracion_y3 = m4 * (y4-y3) / vc
    aceleracion_x4 = m3 * (x2-x4) / vc
    aceleracion_y4 = m3 * (y2-y4) / vc


    velocidad_x1 += aceleracion_x1
    velocidad_y1 += aceleracion_y1
    velocidad_x2 += aceleracion_x2
    velocidad_y2 += aceleracion_y2
    velocidad_x3 += aceleracion_x3
    velocidad_y3 += aceleracion_y3
    velocidad_x4 += aceleracion_x4
    velocidad_y4 += aceleracion_y4

    x1 += velocidad_x1
    y1 += velocidad_y1
    x2 += velocidad_x2
    y2 += velocidad_y2
    y3 += velocidad_y3
    y3 += velocidad_y3
    y4 += velocidad_y4
    y4 += velocidad_y4

    cuerpo1.goto(x1,y1)
    cuerpo2.goto(x2,y2)
    cuerpo3.goto(x3,y3)
    cuerpo4.goto(x4,y4)

pantalla.exitonclick()
