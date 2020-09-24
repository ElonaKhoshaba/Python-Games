from turtle import *
import math
import random

#Creates screen
screen = Screen()
screen.screensize(500,500)
screen.bgcolor("black")
#screen.bgpic("C:\Users\elona\Desktop\space.png")

#Creates border
border=Turtle()
border.hideturtle()
border.penup()
border.setpos(-200,200)
border.pensize(3)
border.pencolor("white")
border.pendown()

#Frame updates
screen.tracer(2.5)

for side in range(4):
        border.fd(400)
        border.right(90)
    
#Creates player
player=Turtle()
player.shapesize(0.5)
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)

#Creat the score variable
score = 0

#Create goals
maxGoals = 5 
goals = []

for count in range(maxGoals):
        goals.append(Turtle())
        goals[count].color("red")
        goals[count].shapesize(0.75)
        goals[count].shape("circle")
        goals[count].penup()
        goals[count].speed(0)
        goals[count].setposition(random.randint(-190, 190), random.randint(-190, 190))

#Creates allies
maxAllies = 5 
allies = []

for count in range(maxAllies):
        allies.append(Turtle())
        allies[count].shapesize(0.75)
        allies[count].color("blue")
        allies[count].shape("square")
        allies[count].penup()
        allies[count].speed(0)
        allies[count].setposition(random.randint(-190, 190), random.randint(-190, 190))

#Set speed variable
speed = 1

#Creates controls
def turnleft():
        player.left(30)

def turnright():
        player.right(30)

def increase_speed():
        global speed
        speed+=1

def decrease_speed():
        global speed
        if speed>1:
                speed-=1

def isCollision(t1,t2):
        d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
        if d<20:
                return True
        else:
                return False

#def shoot():
        
    
#Responds to key presses
listen()
onkey(turnleft,"Left")
onkey(turnright,"Right")
onkey(increase_speed,"Up")
onkey(decrease_speed, "Down")

#Score pen
mypen=Turtle()

while True:
        #Player constantly moves
        player.fd(speed)

        #Boundary checking for player
        if player.xcor() > 200 or player.xcor() < -200:
                player.right(180)

        if player.ycor() > 200 or player.ycor() < -200:
                player.right(180)
                
        #Move the goal
        for count in range(maxGoals):
                goals[count].fd(3)
                allies[count].fd(3)

                #Boundary Checking for Goals
                if goals[count].xcor() > 190 or goals[count].xcor() < -190:
                        goals[count].right(180)
                                
                #Boundary Checking for Goals
                if goals[count].ycor() > 190 or goals[count].ycor() < -190:
                        goals[count].right(180)


                #Boundary Checking for Allies
                if allies[count].xcor() > 190 or allies[count].xcor() < -190:
                        allies[count].right(180)
                                
                #Boundary Checking for Allies
                if allies[count].ycor() > 190 or allies[count].ycor() < -190:
                        allies[count].right(180)
                        

                #Collision checking
                if isCollision(player, goals[count]):
                        goals[count].setposition(random.randint(-190, 190), random.randint(-190, 190))
                        goals[count].right(random.randint(0,360))
                        score += 1

                        mypen.undo()
                        mypen.color("white")
                        mypen.penup()
                        mypen.pensize(3)
                        mypen.hideturtle()
                        mypen.setposition(-200,200)
                        mypen.pendown()
                        scorestring = "Score:" + str(score)
                        mypen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
                        
                if isCollision(player, allies[count]):
                        allies[count].setposition(random.randint(-190, 190), random.randint(-190, 190))
                        allies[count].right(random.randint(0,360))
                        score -= 1
                        
                        #Draw the score on the screen
                        mypen.undo()
                        mypen.color("white")
                        mypen.penup()
                        mypen.pensize(3)
                        mypen.hideturtle()
                        mypen.setposition(-200,200)
                        mypen.pendown()
                        scorestring = "Score:" + str(score)
                        mypen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
                
                     
                        
                


delay = eval(input("Press Enter to finish."))
