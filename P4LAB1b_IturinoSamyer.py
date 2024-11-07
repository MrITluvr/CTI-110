# Samyer Iturrino
# 11/7/24
# PLAB1
# This will make a square and triangle



# Samyer Iturrino
# 11/7/24
# PLAB1
# This will make a my initials S and I


import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)  # Adjust speed as needed
t.pensize(3)  # Set pen size
t.color("blue")  # Choose a color for drawing

# Draw first initial (S)
t.penup()
t.goto(-150, 0)  # Position the turtle at the starting point for the first initial
t.pendown()

# Draw "S" (We will use lines and curves for better control)
t.setheading(180)  # Start by facing right
t.circle(50, 180)  # Draw the top half of "S" (semi-circle to the right)
t.setheading(0)  # Turn to face left
t.circle(-50, 180)  # Draw the bottom half of "S" (semi-circle to the left)
t.setheading(0)  # Start by facing right



# Move to the position for the second initial
t.penup()
t.goto(100, 0)  # Move to the right for the second initial
t.pendown()

# Draw second initial (I)
t.color("green")  # Change color for the second initial

# Draw "I"
t.setheading(90)  # Make sure the turtle is facing upwards
t.forward(100)    # Draw the vertical line of "I"

# Finish up
t.hideturtle()  # Hide the turtle after drawing
screen.mainloop
