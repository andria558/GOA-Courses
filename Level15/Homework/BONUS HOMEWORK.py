from turtle import *

bgcolor("light blue") #making sky (backround)

speed(30)
penup()
goto(-770,10)
pendown()
left(50)
color("green")
begin_fill()
forward(400)   # making muntains (backround)
right(80)
forward(200)
left(85)
forward(100)
right(25)
forward(100)
right(80)
forward(150)
left(65)
forward(150)
left(55)
forward(130)
right(110)
forward(880)
right(50)
forward(700)
right(90)
goto(-770,-700)
right(80)
forward(700)
end_fill()


penup()
goto(-350,-300)
pendown()
right(10)
color("gray")
begin_fill()
forward(300)   # making castle
right(90)
for i in range(4):
    forward(45)
    left(90)
    forward(40)
    right(90)
    forward(45)
    right(90)
    forward(40)
    left(90)
forward(45)
right(90)
forward(300)
right(90)
forward(130)
end_fill()
right(90)
color("brown")
begin_fill()
forward(150) # making a door
circle(70,180)
forward(150)
right(90)
end_fill()
penup()
forward(136) # adding more room
pendown()
right(90)
color("grey")
begin_fill()
forward(450)
right(90)
forward(70)
left(90)
forward(100) #adding detals
forward(50) 
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(45)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(45)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
left(90)
forward(100)
left(90)
forward(55)
right(90)
forward(450)
end_fill()
left(90)
forward(320)
color("black")
left(90)

forward(220)
penup()
goto(55,-295)
pendown()
color("grey")
begin_fill()
forward(450) # making ather room
right(90)
forward(100)
right(90)
forward(455)
right(90)
forward(120)
end_fill()
color("red")
penup()
goto(10,155)
pendown()
right(120)
begin_fill()
forward(165)  #making triangle
right(115)
forward(175)
right(125)
forward(184)
end_fill()
penup()   # making a mini flag
right(120)
color("black")
forward(167)
left(30)
pendown()
begin_fill()
forward(60)
right(110)
forward(50)
right(135)
forward(55)
color("yellow")
end_fill()
penup()
goto(1234,1234)
pendown()



exitonclick()


