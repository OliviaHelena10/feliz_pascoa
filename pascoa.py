import turtle

# Create a screen for drawing
screen = turtle.Screen()
screen.title("Easter Egg with Bunny")
screen.bgcolor("lightblue")

# Create a turtle for drawing the egg
egg_turtle = turtle.Turtle()
egg_turtle.speed(8)

# Draw the Easter egg
egg_turtle.penup()
egg_turtle.goto(0, -200)
egg_turtle.pendown()
egg_turtle.color("purple")
egg_turtle.begin_fill()
egg_turtle.circle(200)
egg_turtle.end_fill()

# Draw patterns on the egg
egg_turtle.penup()
egg_turtle.goto(-180, -200)
egg_turtle.pendown()
egg_turtle.color("yellow")
egg_turtle.begin_fill()
egg_turtle.circle(50)
egg_turtle.end_fill()

egg_turtle.penup()
egg_turtle.goto(150, -100)
egg_turtle.pendown()
egg_turtle.color("pink")
egg_turtle.begin_fill()
egg_turtle.circle(80)
egg_turtle.end_fill()

# Create a turtle for drawing the bunny
bunny_turtle = turtle.Turtle()
bunny_turtle.speed(2)

# Draw the bunny's body
bunny_turtle.penup()
bunny_turtle.goto(-40, -100)
bunny_turtle.pendown()
bunny_turtle.color("white")
bunny_turtle.begin_fill()
bunny_turtle.circle(50)
bunny_turtle.end_fill()

# Draw the bunny's head
bunny_turtle.penup()
bunny_turtle.goto(-30, 0)
bunny_turtle.pendown()
bunny_turtle.color("white")
bunny_turtle.begin_fill()
bunny_turtle.circle(35)
bunny_turtle.end_fill()

# Draw the bunny's ears
def draw_ear1(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.setheading(100)
    turtle.circle(100, 50)
    turtle.end_fill()

def draw_ear2(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.setheading(30)
    turtle.circle(100, 50)
    turtle.end_fill()

draw_ear1(bunny_turtle, -30, 70)
draw_ear2(bunny_turtle, -20, 70)

# Draw the bunny's eyes
bunny_turtle.penup()
bunny_turtle.goto(-45, 40)
bunny_turtle.pendown()
bunny_turtle.color("black")
bunny_turtle.dot(10)

bunny_turtle.penup()
bunny_turtle.goto(-20, 40)
bunny_turtle.pendown()
bunny_turtle.color("black")
bunny_turtle.dot(10)

# Draw the bunny's nose
bunny_turtle.penup()
bunny_turtle.goto(-35, 30)
bunny_turtle.pendown()
bunny_turtle.color("pink")
bunny_turtle.dot(5)

# Draw the bunny's mouth
bunny_turtle.penup()
bunny_turtle.goto(-45, 20)
bunny_turtle.pendown()
bunny_turtle.setheading(270)
bunny_turtle.circle(10, 180)

# Draw the bunny's arm1
bunny_turtle.penup()
bunny_turtle.goto(-70, -40)
bunny_turtle.pendown()
bunny_turtle.color("grey")
bunny_turtle.setheading(270)
bunny_turtle.circle(7, 180)

# Draw the bunny's arm2
bunny_turtle.penup()
bunny_turtle.goto(-30, -40)
bunny_turtle.pendown()
bunny_turtle.color("grey")
bunny_turtle.setheading(270)
bunny_turtle.circle(7, 180)

# Draw the bunny's leg1
bunny_turtle.penup()
bunny_turtle.goto(-30, -70)
bunny_turtle.pendown()
bunny_turtle.color("grey")
bunny_turtle.setheading(270)
bunny_turtle.circle(7, 180)

# Draw the bunny's leg2
bunny_turtle.penup()
bunny_turtle.goto(-70, -70)
bunny_turtle.pendown()
bunny_turtle.color("grey")
bunny_turtle.setheading(270)
bunny_turtle.circle(7, 180)

# Hide the turtles and display the final result
egg_turtle.hideturtle()
bunny_turtle.hideturtle()
turtle.done()