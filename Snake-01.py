import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# מסך
wn = turtle.Screen()
wn.title("maya shemer python project")
wn.bgcolor('yellow')
wn.bgpic('bakrownd.gif')
wn.setup(1.0, 1.0)
wn.tracer(0)  # Turns off the screen updates
wn.addshape('snake-byde.gif')
wn.addshape('haed-dun-01.gif')
wn.addshape('apple.gif')
wn.addshape('haed-reth-01.gif')
wn.addshape('haed-up-01.gif')
wn.addshape('head-left-1.gif')

# score board
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score : 0  High Score : 0", align="center",
          font=("candara", 24, "bold"))

# ראש הנחש
head = turtle.Turtle()
head.speed(0)
head.shape('head-left-1.gif')
head.penup()
head.goto(0, 0)
head.direction = "stop"

# אוכל
food = turtle.Turtle()
food.speed(0)
food.shape("apple.gif")
food.penup()
food.goto(0, 100)

segments = []


# פקודות
def go_up():
    if head.direction != "down":
        head.direction = "up"



def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"



def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        head.shape('haed-up-01.gif')

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        head.shape('haed-dun-01.gif')

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        head.shape('head-left-1.gif')

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        head.shape('haed-reth-01.gif')


# חיבור למקלדת
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

while True:
    wn.update()

    # לבדוק התנגשות בצידי המסך
    if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 190 or head.ycor() < -190:
        time.sleep(1)
        head.shape('head-left-1.gif')
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        delay = 0.1

        score = 0
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

    # לבדוק נפגש עם אוכל
    if head.distance(food) < 20:
        # העברת אוכל למקום רנדולי על המסך
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        food.goto(x, y)

        # גוף הנחש
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("snake-byde.gif")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # בדיקה של מפגש של הראש עם הגוף
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.shape('head-left-1.gif')
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            delay = 0.1

            score = 0
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

wn.mainloop
