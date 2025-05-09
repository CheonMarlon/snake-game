import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=700, height=700)

turtle.speed(10)
turtle.pensize(1)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("white")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

food = turtle.Turtle()
food_color = random.choice(['yellow', 'orange', 'red'])
food_shape = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(food_shape)
food.color(food_color)
food.penup()
food.goto(random.randint(-290, 290), random.randint(-240, 240))

scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape("square")
scoreBoard.color("white")
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 250)
scoreBoard.write("Score: 0 High Score: 0", align="center", font=("courier", 25, "bold"))

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

segments = []

def reset_game():
    global score, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Stop"
    for segment in segments:
        segment.goto(1000, 1000)  # Move segments off-screen
    segments.clear()
    score = 0
    delay = 0.1
    scoreBoard.clear()
    scoreBoard.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 25, "bold"))

while True:
    wn.update()

    # Boundary collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 240 or head.ycor() < -240:
        reset_game()

    # Collision with food
    if head.distance(food) < 20:
        score += 10
        delay -= 0.001  # Speed up the snake slightly
        if score > high_score:
            high_score = score

        scoreBoard.clear()
        scoreBoard.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("courier", 25, "bold"))

        x_cord = random.randint(-290, 290)
        y_cord = random.randint(-240, 240)
        food_color = random.choice(['yellow', 'orange', 'red'])
        food_shape = random.choice(['square', 'triangle', 'circle'])
        food.shape(food_shape)
        food.color(food_color)
        food.goto(x_cord, y_cord)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white smoke")
        new_segment.penup()
        segments.append(new_segment)


    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)


    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()


    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    time.sleep(delay)
