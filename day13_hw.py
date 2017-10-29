import turtle as timport random
t.shape("turtle")t.speed(0)t.up() t.goto(-475,400)t.down() 
for x in range(4):    t.fd(500)    t.rt(90)
t.up()t.goto(-225,150)t.down()
a = random.randint(1, 360) 
t.lt(a)
while -100 <= t.ycor() <= 400 and -475 <= t.xcor() <= 25:    t.fd(1)    if t.ycor() >= 400:        ang = t.heading()        if 0 <= t.heading() <= 90:            t.rt(2*ang)            t.fd(10)        else:            t.lt(-2*ang)            t.fd(10)    if t.ycor() <= -100:        ang = t.heading()        if 180 <= t.heading() <= 270:            t.rt(2*ang)            t.fd(10)        else:            t.lt(-2*ang)            t.fd(10)    if t.xcor() >= 25:        ang = t.heading()        if 270 <= t.heading() <= 360:            t.rt(2*ang - 180)            t.fd(10)        else:            t.lt(180 - 2*ang)            t.fd(10)    if t.xcor() <= -475:        ang = t.heading()        if 90 <= t.heading() <= 180:            t.rt(2*ang - 180)            t.fd(10)        else:            t.lt(180 - 2*ang)            t.fd(10)
