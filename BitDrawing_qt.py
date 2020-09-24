from turtle import *

######################DEFINING VARIABLES#####################
w = "white"
b = "black"
r = "red"
p = "purple"
g = "gray"

    
def grid():
    yaxis=170
    for i in range(19):
        goto(-290,yaxis)
        for i in range(29):
            pixel()
            fd(20)
        penup()
        yaxis-=20
    
def pixel():
    pendown() 
    for i in range(4):
        fd(20)
        left(90)

def dot(lista):
    x=0
    for i in range(29):
        color(lista[x])
        begin_fill()
        pixel()
        end_fill()
        fd(20)
        x+=1


####################ACTUAL CODE###############################

tracer(-100,100)

##grid() 

listx=[[w,w,b,b,b,b,w,w,w,b,b,b,b,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,b,r,r,r,r,b,w,b,r,r,r,r,b,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [b,r,r,w,w,r,r,b,r,r,r,r,r,r,b,w,w,b,b,w,w,w,b,w,w,w,w,w,w],
       [b,r,w,w,r,r,r,r,r,r,r,r,r,r,b,w,b,w,w,b,w,w,b,w,w,w,w,w,w],
       [b,r,w,r,r,r,r,r,r,r,r,r,r,r,b,w,w,b,b,b,w,b,b,b,w,w,w,w,w],
       [b,r,r,r,r,r,r,r,r,r,r,r,r,r,b,w,w,w,w,b,w,w,b,w,w,w,w,w,w],
       [b,r,r,r,r,r,r,r,r,r,r,r,r,r,b,w,w,w,w,b,w,w,b,w,w,w,w,w,w],
       [w,b,r,r,r,r,r,r,r,r,r,r,r,b,w,w,w,w,w,b,w,w,b,b,w,w,w,w,w],
       [w,w,b,r,r,r,r,r,r,r,r,r,b,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,b,r,r,r,r,r,r,r,b,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,w,b,r,r,r,r,r,b,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,w,w,b,r,r,r,b,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,w,w,w,b,r,b,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,w,w,w,w,b,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w],
       [w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w,w]]

yaxis=170
y=0
for i in range(19):
    penup()
    goto(-290,yaxis)
    pendown()
    dot(listx[y])
    yaxis-=20
    y+=1





######################FOR MY REFERENCE###############################


##penup()
##for i in range(2):
##    fd(10)
##    left(90)

##def grid():
##    for i in range(15):
##        pixel()
##        fd(20)
##    penup()
##    goto(10,-10)
##    left(180)
##
##    for i in range(14):
##        pixel()
##        fd(20)
##    penup()
##    goto(10,10)
##    left(90)
##
##    for i in range(9):
##        pixel()
##        fd(20)
##
##    penup()
##    goto(-10,-10)
##    left(180)
##
##
##    for i in range(9):
##        pixel()
##        fd(20)



