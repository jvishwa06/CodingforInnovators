import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Create a turtle named "house"
house = turtle.Turtle()
house.speed(2)

# Draw the base of the house
house.penup()
house.goto(-100, -100)
house.pendown()
house.color("blue")
house.begin_fill()
for _ in range(4):
    house.forward(200)
    house.left(90)
house.end_fill()

# Draw the roof
house.color("red")
house.begin_fill()
house.left(45)
house.forward(141)
house.right(90)
house.forward(141)
house.right(135)
house.forward(200)
house.end_fill()

# Draw the door
house.penup()
house.goto(-30, -100)
house.pendown()
house.color("brown")
house.begin_fill()
house.setheading(90)
house.forward(100)
house.right(90)
house.forward(60)
house.right(90)
house.forward(100)
house.end_fill()

# Draw a window
house.penup()
house.goto(-70, 0)
house.pendown()
house.color("white")
house.begin_fill()
for _ in range(4):
    house.forward(40)
    house.right(90)
house.end_fill()

# Hide the turtle
house.hideturtle()

# Keep the window open until clicked
screen.exitonclick()