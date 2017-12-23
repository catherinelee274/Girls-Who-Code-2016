from turtle import *
penup()
goto(-500,-100)
pendown()
def drawSquare(times):
    for i in range(times):
        for i in range(4):
            pencolor("SkyBlue")
            forward(50)
            left(90)
        forward(100)

    
    return times

drawSquare(16)
