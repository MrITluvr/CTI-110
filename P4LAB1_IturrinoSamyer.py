# Samyer Iturrino
# 11/7/24
# PLAB1
# This will make a square and triangle


import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)  # You can adjust the speed of drawing here

# Draw a square
for _ in range(4):  # Loop to draw the square
    t.forward(100)  # Move turtle forward by 100 units
    t.left(90)      # Turn the turtle left by 90 degrees

# Move the turtle to a new position without drawing
t.penup()
t.forward(150)
t.pendown()

# Draw a triangle
for _ in range(3):  # Loop to draw the triangle
    t.forward(100)  # Move turtle forward by 100 units
    t.left(120)     # Turn the turtle left by 120 degrees

# Finish up
t.hideturtle()  # Hide the turtle afte
