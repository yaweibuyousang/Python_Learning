#digitLED.py
import turtle as t
import time as ti

def drawGap():
    t.penup()
    t.fd(5)

def drawPoint():
    t.pencolor("red")
    t.penup()
    t.left(90)
    t.fd(19)
    t.pendown()
    t.fd(1)
    t.penup()
    t.right(180)
    t.fd(39)
    t.pendown()
    t.fd(1)
    t.penup()
    t.left(180)
    t.fd(20)
    

def drawLine(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)

def drawDigit(digit):
    t.pencolor("blue")
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0,4,5,6,8] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)

def dealChar(string):
    sp = string.split(" ")
    for i in sp[4]:
        drawDigit(eval(i))
    t.fd(40)

    dateT=sp[3].split(":")
    for i in range(3):
        for j in dateT[i]:
            drawDigit(eval(j))
        if i<2:
            drawPoint()
            t.right(90)
            t.fd(20)
    t.fd(40)
    t.pencolor("orange")
    t.write(sp[0],font=("Arial",18,"normal"))
    t.fd(60)
    t.write(sp[1],font=("Arial",18,"normal"))
    t.fd(40)
    t.write(sp[2],font=("Arial",18,"normal"))    

def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    dealChar(ti.ctime())
    t.hideturtle()
    t.done()

main()

