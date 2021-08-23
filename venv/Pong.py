import turtle

win=turtle.Screen()
win.colormode(255)
win.bgcolor(61, 64, 91)
win.title("Play Pong by @Floydaritra")
win.setup(width=800,height=600)
win.tracer(0)

#main scoring
s1=0
s2=0

#Title
image="name.gif"
win.register_shape(image)
t=turtle.Turtle()
t.speed(0)
t.shape(image)
t.penup()
t.goto(0,0)

#gameover screen
image2="gameover1.gif"
win.register_shape(image2)
g=turtle.Turtle()
g.speed(0)
g.shape(image2)
g.penup()
g.goto(0,700)
image3="gameover2.gif"
win.register_shape(image3)
g2=turtle.Turtle()
g2.speed(0)
g2.shape(image3)
g2.penup()
g2.goto(0,700)

#score
sc=turtle.Turtle()
sc.speed(0)
sc.color(129, 178, 154)
sc.penup()
sc.hideturtle()
sc.goto(0,225)
sc.write("0\t0",align="center",font=("STCaiyun",40,"bold"))

split=turtle.Turtle()
split.speed(0)
split.shape("square")
split.color(242, 204, 143)
split.shapesize(stretch_wid=40,stretch_len=0.15)
split.penup()
split.goto(0,0)

#1st paddle
p1=turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color(244, 241, 222)
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(-350,0)

#2nd paddle
p2=turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color(244, 241, 222)
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(350,0)

#ball
b=turtle.Turtle()
b.speed()
b.shape("circle")
b.color(231, 111, 81)
b.penup()
b.goto(0,0)
b.dx=0
b.dy=0

#moving the paddles
def p1up():
    y=p1.ycor()
    y+=10
    p1.sety(y)

def p1down():
    y=p1.ycor()
    y-=10
    p1.sety(y)

def p2up():
    y=p2.ycor()
    y+=10
    p2.sety(y)

def p2down():
    y=p2.ycor()
    y-=10
    p2.sety(y)

#starting
def starting():
    t.goto(0,700)
    b.dx = 0.25
    b.dy = 0.25

#key bindings
win.listen()
win.onkeypress(starting," ")
win.onkeypress(p1up,"w")
win.onkeypress(p1down,"s")

win.onkeypress(p2up,"Up")
win.onkeypress(p2down,"Down")


#main loop
while True:
    win.update()

    b.setx(b.xcor()+b.dx)
    b.sety(b.ycor()+b.dy)

    if b.ycor() > 290:
        b.sety(290)
        b.dy *= -1

    if b.ycor() < -290:
        b.sety(-290)
        b.dy *= -1

    if b.xcor() > 390:
        b.goto(0,0)
        b.dx *= -1
        s1+=1
        sc.clear()
        sc.write("{}\t{}".format(s1,s2), align="center", font=("STCaiyun", 40, "bold"))

    if b.xcor() < -390:
        b.goto(0,0)
        b.dx *= -1
        s2+=1
        sc.clear()
        sc.write("{}\t{}".format(s1, s2), align="center", font=("STCaiyun", 40, "bold"))

    if (b.xcor() > 340 and b.xcor() <350) and (b.ycor() < p2.ycor()+50 and b.ycor() > p2.ycor()-50):
        b.setx(340)
        b.dx *= -1

    if (b.xcor() < -340 and b.xcor() > -350) and (b.ycor() < p1.ycor()+50 and b.ycor() > p1.ycor() -50):
        b.setx(-340)
        b.dx *= -1

    if p1.ycor()>350:
        p1.goto(-350,-330)
    if p1.ycor()<-350:
        p1.goto(-350,330)
    if p2.ycor()>350:
        p2.goto(350,-330)
    if p2.ycor()<-350:
        p2.goto(350,330)
    if s1 == 3:
        g.goto(-25,0)
        b.goto(0,0)
        b.dx=0
        b.dy=0
    if s2 == 1:
        g2.goto(-25,0)
        b.goto(0,0)
        b.dx=0
        b.dy=0