import random
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)  

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("white")

dots = [[random.randint(-200, 200), random.randint(-200, 200), random.uniform(0.5, 2.0)] for _ in range(20)]

while True:
    t.clear()  
    for dot in dots:
        dot[1] += dot[2]  
        if dot[1] > 200:  
            dot[1] = -200
            dot[0] = random.randint(-200, 200)
        
        t.goto(dot[0], dot[1])
        t.dot(5)  # Draw a 5px white dot
        
    screen.update()  
