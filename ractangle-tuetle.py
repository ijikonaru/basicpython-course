from turtle import *
import turtle
t = turtle.Pen() #ดึงความสามารถการใช้ปากกา
t.shape('turtle')#แปลงร่างเป้นเต่า

def Rectangle():
    '''ฟังชั่นนี้เอาไว้วาดรูปสี่เหลี่ยม'''
    for i in range(4):
        t.fd(100)
        t.lt(90)

def Go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    

def Redians(s=50,f=10):
    t.color('red', '#99F4FF')
    t.begin_fill()
    fq= 360/f
    t.speed(1000000)
    for i in range(f):
        t.circle(s)
        t.lt(fq)
    t.end_fill()

def RSquare(s=50,f=10):
    t.color('blue', 'green')
    t.begin_fill()
    fq= 360/f
    t.speed(1000000)
    for i in range(f):
        Rectangle()
        t.lt(fq)
    t.end_fill()

RSquare()
    
Go(-200,-200)
Redians()

Go(200,-200)
Redians(40,20)

Go(200,200)
Redians()

Go(-200,200)
Redians(60,30)
