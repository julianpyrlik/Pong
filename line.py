from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.setposition(x=0, y=-250)
        self.pendown()
        self.setheading(90)
        self.drawline()
        self.drawline()

    def drawline(self):
        for move in range(15):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()






