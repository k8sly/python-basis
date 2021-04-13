import turtle


def Write():
    # printer = turtle.Turtle()
    # printer.hideturtle()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.back(100)
    turtle.pencolor('red')
    turtle.write("Rose for you!\n\n", align="right", font=("楷体", 20, "bold"))
    turtle.pencolor('black')
    turtle.write("            from LY", align="right", font=("楷体", 16, "normal"))


def rose():  # 花蕊
    turtle.pencolor("pink")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10, 180)
    turtle.circle(25, 110)
    turtle.left(50)
    turtle.circle(60, 45)
    turtle.circle(20, 170)
    turtle.right(24)
    turtle.fd(30)
    turtle.left(10)
    turtle.circle(30, 110)
    turtle.fd(20)
    turtle.left(40)
    turtle.circle(90, 70)
    turtle.circle(30, 150)
    turtle.right(30)
    turtle.fd(15)
    turtle.circle(80, 90)
    turtle.left(15)
    turtle.fd(45)
    turtle.right(165)
    turtle.fd(20)
    turtle.left(155)
    turtle.circle(150, 80)
    turtle.left(50)
    turtle.circle(150, 90)
    turtle.end_fill()


def rose1():
    turtle.pencolor("pink")
    # 花瓣1
    turtle.left(150)
    turtle.circle(-90, 70)
    turtle.left(20)
    turtle.circle(75, 105)
    turtle.setheading(60)
    turtle.circle(80, 98)
    turtle.circle(-90, 40)


def rose2():
    turtle.pencolor("pink")
    # 花瓣2
    turtle.left(180)
    turtle.circle(90, 40)
    turtle.circle(-80, 98)
    turtle.setheading(-83)


def leaf1():
    turtle.pencolor("brown4")
    turtle.pensize(2)
    # 叶子1
    turtle.fd(30)
    turtle.pencolor("green")
    turtle.left(90)
    turtle.fd(25)
    turtle.left(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(-80, 90)
    turtle.right(90)
    turtle.circle(-80, 90)
    turtle.end_fill()
    turtle.pencolor("brown4")
    turtle.pensize(2)
    turtle.right(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(85)
    turtle.left(90)
    turtle.fd(80)


def leaf2():
    turtle.pencolor("green")
    # 叶子2
    turtle.right(90)
    turtle.right(45)
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(80, 90)
    turtle.left(90)
    turtle.circle(80, 90)
    turtle.end_fill()
    turtle.pencolor("brown4")
    turtle.pensize(2)
    turtle.left(135)
    turtle.fd(60)
    turtle.left(180)
    turtle.fd(60)
    turtle.right(90)
    turtle.circle(200, 60)


def drawRose():
    # turtle.delay(0)
    # 设置初始位置
    turtle.hideturtle()
    turtle.penup()
    turtle.left(90)
    turtle.fd(200)
    turtle.pendown()
    turtle.right(90)
    rose()
    rose1()
    rose2()
    leaf1()
    leaf2()
    Write()


drawRose()
turtle.done()
