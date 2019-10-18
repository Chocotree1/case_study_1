#Developers: Zaytsev A. 40%
#            Sharypov R.
#            Kurasova P.
import turtle
turtle.setup(1020,640)
#TODO ALEXANDER
#boat
#trapezoid
turtle.speed(0)
turtle.goto(0,0)
turtle.pendown()
turtle.fillcolor('grey')
turtle.begin_fill()
turtle.forward(300)
turtle.right(135)
turtle.forward(105)
turtle.right(45)
turtle.forward(150)
turtle.right(45)
turtle.forward(105)
turtle.end_fill()
turtle.up()
# rectangle
turtle.right(135)
turtle.forward(50)
turtle.pendown()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()
turtle.up()
#triangle1
turtle.left(90)
turtle.forward(60)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.left(90)
turtle.forward(70)
turtle.right(135)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(135)
turtle.end_fill()
turtle.up()
#triangle2
turtle.forward(70)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.forward(50)
turtle.right(135)
turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.right(135)
turtle.end_fill()
turtle.up()
#square
turtle.right(180)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.end_fill()
turtle.up()

#circles
turtle.forward(140)
turtle.right(90)
turtle.forward(120)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.up()
turtle.forward(20)
turtle.right(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(10)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.up()

#house
#rectangle
turtle.goto(150,150)
turtle.right(90)
turtle.forward(40)
turtle.pendown()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(120)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(120)
turtle.end_fill()
turtle.up()
#trapezoid
turtle.right(90)
turtle.forward(60)
turtle.left(90)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.forward(40)
turtle.right(135)
turtle.forward(80)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(80)
turtle.right(135)
turtle.forward(90)
turtle.end_fill()
turtle.up()

#triangle1
turtle.left(90)
turtle.forward(40)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.right(90)
turtle.forward(60)
turtle.right(135)
turtle.forward(42)
turtle.right(90)
turtle.forward(42)
turtle.end_fill()
turtle.up()

#trianle2
turtle.left(135)
turtle.forward(50)
turtle.left(90)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.forward(60)
turtle.right(135)
turtle.forward(42)
turtle.right(90)
turtle.forward(42)
turtle.end_fill()
turtle.up()

#square
turtle.left(135)
turtle.forward(47)
turtle.pendown()
turtle.fillcolor('grey')
turtle.begin_fill()
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.end_fill()
turtle.up()

#circles
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(15)
turtle.left(90)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.up()


turtle.right(90)
turtle.forward(10)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.up()












#TODO POLINA
#Snegovik :)
#circle
turtle.goto(-30,200)
turtle.setheading (270)
turtle.forward(200)
turtle.setheading(180)
turtle.forward(350)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.up()
#kvadrat
turtle.right(180)
turtle.forward(45)
turtle.right(180)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.forward(90)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(25)
turtle.end_fill()
turtle.up()
#circlesmall
turtle.right(90)
turtle.forward(155)
turtle.left(100)
turtle.forward(25)
turtle.pendown()
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.up()
#treygolniksmall
turtle.right(180)
turtle.forward(20)
turtle.right(180)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.forward(50)
turtle.right(135)
turtle.forward(35)
turtle.right(90)
turtle.forward(35)
turtle.right(135)
turtle.end_fill()
turtle.up()
#ruka1

turtle.pendown
turtle.right(240)
turtle.forward(90)
turtle.right(90)
turtle.forward(23)
turtle.pendown()
turtle.fillcolor('purple')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
turtle.up()
 #ruka 2
turtle.right(40)
turtle.forward(100)
turtle.pendown
turtle.fillcolor('purple')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
turtle.up()
#metla
turtle.right(270)
turtle.forward(270)
turtle.pendown()
turtle.right(180)
turtle.pensize(5)
turtle.forward(350)
turtle.right(45)
turtle.forward(50)
turtle.up()
turtle.right(180)
turtle.forward(50)
turtle.pendown()
turtle.right(90)
turtle.forward(50)
turtle.up()
turtle.right(180)
turtle.forward(50)
turtle.right(220)
turtle.pendown()
turtle.forward(50)


#TODO Roman
#simple flower
def flower (x,y,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(90)
    turtle.color('green')
    turtle.pendown()
    turtle.fd(200)
    turtle.setheading(0)
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.circle(20,360)
    turtle.end_fill()
    for i in range(4):
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(-35,360)
        turtle.end_fill()
        turtle.color('yellow')
        turtle.circle(20,90)
flower(-100,0,'red')


#difficult flower
#polygon
turtle.up()
turtle.goto(-200,-150)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(50)
turtle.right(60)
turtle.end_fill()

#triangles for petals
turtle.up()
turtle.goto(-200,-150)
turtle.pendown()
turtle.pencolor('green')
turtle.fillcolor('green')
turtle.begin_fill()
turtle.left(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.end_fill()

#center of the flower
turtle.up()
turtle.goto(-175,-212)
turtle.pendown()
turtle.pencolor('red')
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(20,360)
turtle.end_fill()




turtle.mainloop()
































