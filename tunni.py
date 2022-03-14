#tunni2
#Karl Jugapuu

import turtle

aken = turtle.Screen()
aken.setup(300, 300)
aken.title("kodu - Karl Jugapuu")

t = turtle.Turtle()

for i in range(0, 10):
    
    if i <= 3:
        
        t.forward(100)
        t.lt(90)
        
    elif i <= 5:
        
        t.forward(50)
        t.lt(90)
        
    elif i <= 10:
        
        t.forward(100)
        t.lt(90)

turtle.exitonclick()