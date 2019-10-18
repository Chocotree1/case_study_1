#Developers: Zaytsev A. 40%
#            Sharypov R. 50% (because of debuging)
#            Kurasova P. 40%
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
#Snowman

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

#square
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

#small circle
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

#small triangles
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

#first hand
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

#second hand
turtle.right(40)
turtle.forward(100)
turtle.pendown
turtle.fillcolor('purple')
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
turtle.up()

#broom
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

#flower
turtle.up()
turtle.goto(500,-100)
turtle.pensize(2)
turtle.forward(180)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()
turtle.up()
turtle.forward(30)
turtle.left(90)
turtle.forward(20)
turtle.pendown()
turtle.fillcolor('orange')
turtle.begin_fill()
turtle.right(90)
turtle.forward(60)
turtle.right(135)
turtle.forward(42)
turtle.right(90)
turtle.forward(42)
turtle.end_fill()
turtle.up()
turtle.forward(30)
turtle.left(90)
turtle.forward(55)
turtle.pendown()
turtle.fillcolor('orange')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.up()
turtle.right(90)
turtle.forward(60)
turtle.fillcolor('pink')
turtle.begin_fill()
turtle.right(90)
turtle.forward(60)
turtle.right(135)
turtle.forward(42)
turtle.right(90)
turtle.forward(42)
turtle.end_fill()
turtle.up()
turtle.right(180)
turtle.forward(115)
turtle.pendown()
turtle.fillcolor('purple')
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.up()
turtle.right(180)
turtle.forward(10)
turtle.right(180)
turtle.pendown()
turtle.pensize(5)
turtle.forward(200)
turtle.up()
turtle.right(180)
turtle.forward(100)
turtle.right(90)
turtle.pendown()
turtle.fillcolor('green')
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
turtle.left(360)
turtle.forward(30)
turtle.left(90)
turtle.pendown()
turtle.fillcolor('green')
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

#heavy weapon
#polygon
turtle.up()
turtle.goto(-200,-150)
turtle.pencolor('grey')
turtle.pendown()
turtle.fillcolor('grey')
turtle.begin_fill()
turtle.forward(30)
turtle.right(60)
turtle.forward(30)
turtle.right(60)
turtle.forward(30)
turtle.right(60)
turtle.forward(30)
turtle.right(60)
turtle.forward(30)
turtle.right(60)
turtle.forward(30)
turtle.right(60)
turtle.end_fill()

#triangles for petals of the weapon
turtle.up()
turtle.goto(-200,-150)
turtle.pendown()
turtle.pencolor('black')
turtle.fillcolor('black')
turtle.begin_fill()
turtle.left(60)
turtle.forward(30)
turtle.right(120)
turtle.forward(30)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(30)
turtle.right(120)
turtle.forward(30)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(30)
turtle.right(120)
turtle.forward(30)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(30)
turtle.right(120)
turtle.forward(30)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(30)
turtle.right(120)
turtle.forward(30)
turtle.end_fill()
turtle.begin_fill()
turtle.left(60)
turtle.forward(30)
turtle.right(120)
turtle.forward(30)
turtle.end_fill()

#center of the weapon
turtle.up()
turtle.goto(-185,-185)
turtle.pendown()
turtle.pencolor('red')
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(10,360)
turtle.end_fill()

#weapon handle
turtle.up()
turtle.goto(-170,-205)
turtle.pendown()
turtle.pencolor('black')
turtle.right(60)
turtle.width(10)
turtle.forward(100)
turtle.up()

#Ice cream
turtle.up()
turtle.goto(0,-200)
turtle.pendown()
turtle.pencolor('green')
turtle.fillcolor('green')
turtle.width(1)
turtle.begin_fill()
turtle.left(60)
turtle.forward(50)
turtle.right(60)
turtle.forward(20)
turtle.right(120)
turtle.forward(70)
turtle.right(120)
turtle.forward(20)
turtle.end_fill()
turtle.right(180)
turtle.forward(20)
turtle.pencolor('brown')
turtle.fillcolor('brown')
turtle.begin_fill()
turtle.left(60)
turtle.forward(70)
turtle.left(120)
turtle.forward(70)
turtle.end_fill()
turtle.left(120)
turtle.forward(20)
turtle.pencolor('red')
turtle.fillcolor('red')
turtle.begin_fill()
turtle.forward(30)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(10)
turtle.end_fill()
turtle.up()
turtle.goto(45,-200)
turtle.pendown()
turtle.pencolor('blue')
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(20,180)
turtle.end_fill()
turtle.up

turtle.mainloop()




































