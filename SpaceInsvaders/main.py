import turtle

# Screeni yarattık
window = turtle.Screen()
window.setup(0.5, 0.75)
window.bgcolor(0.2, 0.2, 0.2)
window.title("Space Invaders")

LEFT = -window.window_width() / 2
RIGHT = window.window_width() / 2
TOP = window.window_width() / 2
BOTTOM = -window.window_height() / 2
FLOOR_LEVEL = 0.9 * BOTTOM
GUTTER = 0.025 * window.window_width()

# lazeri yarattık
cannon = turtle.Turtle()
cannon.penup()
cannon.color(1, 1, 1)
cannon.shape("square")
cannon.setposition(0, FLOOR_LEVEL)

# lazer boyutu
cannon.turtlesize(1, 4)
cannon.stamp()
cannon.sety(FLOOR_LEVEL + 10)
cannon.turtlesize(1, 1.5)
cannon.stamp()
cannon.sety(FLOOR_LEVEL + 20)
cannon.turtlesize(0.8, 0.3)
cannon.stamp()
cannon.sety(FLOOR_LEVEL)

lasers = []

def draw_cannon():
    window.update()
    cannon.clear()
    cannon.turtlesize(1, 4)
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 10)
    cannon.turtlesize(1, 1.5)
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 20)
    cannon.turtlesize(0.8, 0.3)
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL)


# lazer hareketi

CANNON_STEP = 30
window.tracer(0) #çizim hızlandırıldı  Bu, çizimlerin biriktirilmesini ve daha sonra tek seferde ekrana yansıtılmasını sağlar,,update ile ekrana yansıtıldı


def move_left():
    new_x =cannon.xcor() - CANNON_STEP
    if new_x >= LEFT + GUTTER:
        cannon.setx(new_x)
        draw_cannon()




def move_right():
    new_x = cannon.xcor() + CANNON_STEP
    if new_x <= RIGHT - GUTTER:
        cannon.setx(new_x)
        draw_cannon()


def create_laser():
    laser = turtle.Turtle()
    laser.penup()
    laser.color(1, 0, 0)
    laser.hideturtle() #turtle ı gizler
    laser.setposition(cannon.xcor(), cannon.ycor())
    laser.setheading(90)
    laser.forward(20)
    laser.pendown()
    laser.pensize(5)

    lasers.append(laser)





window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
window.onkeypress(turtle.bye, "q")
window.onkeypress(create_laser , "space")
window.listen()


draw_cannon()
turtle.done()
