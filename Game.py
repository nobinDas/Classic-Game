import math
import turtle
import random

win = turtle.Screen()
win.bgcolor("black")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-200, -200)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(400)
    border_pen.lt(90)
border_pen.hideturtle()

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()

score = 0
total_score_pen = turtle.Turtle()
total_score_pen.speed(0)
total_score_pen.color("white")
total_score_pen.penup()
total_score_pen.hideturtle()
total_score_pen.setposition(-290, 280)
scoreString = "Score: %s" % score
total_score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))


def is_collision(t1, cor):
    x = cor[0]
    y = cor[1]
    distance = math.sqrt(math.pow(t1.xcor() - x, 2) + math.pow(t1.ycor() - y, 2))
    if distance < 10:
        return True
    else:
        return False


x = -184
y = 185
cubes = []
red_cubes = []
gapCount = 0
gapCheck = random.randint(25, 32)
done = 1
for i in range(17):
    for j in range(17):
        if gapCount == gapCheck:
            gapCheck = random.randint(25, 32)
            cube_red = turtle.Turtle()
            cube_red.color("red")
            cube_red.shape("square")
            cube_red.penup()
            cube_red.speed(0)
            cube_red.setposition(x, y)
            red_cubes.append(cube_red)
            gapCount = 0
            done = 0
        if done == 1:
            cube = turtle.Turtle()
            cube.color("grey")
            cube.shape("square")
            cube.penup()
            cube.speed(0)
            cube.setposition(x, y)
            cubes.append(cube)
        done = 1
        gapCount += 1
        x = x+23
    y = y-23
    x = -184


def explode(x, y):
    global score
    cor = [x, y]
    for cube in cubes:
        if is_collision(cube, cor):
            cube.hideturtle()
            score_pen.setposition(cube.xcor()-2, cube.ycor()-7)
            num = random.randint(1, 4)
            scoreS = "%s" % num
            score_pen.write(scoreS, False, align="left", font=("Arial", 10, "normal"))
            total_score_pen.setposition(-290, 280)
            score = score+num
            scoreString = "Score: %s" % score
            total_score_pen.clear()
            total_score_pen.write(scoreString, False, align="left", font=("Arial", 14, "normal"))
    for cube_red in red_cubes:
        if is_collision(cube_red, cor):
            print("GAME OVER and total score is " + str(score))
            win.bye()


win.onclick(explode)

turtle.mainloop()

