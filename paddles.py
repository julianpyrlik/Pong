from turtle import Turtle

LEFT_PADDLE_POSITIONS = [(-290, -40), (-290, -20), (-290, 0), (-290, 20), (-290, 40)]
RIGHT_PADDLE_POSITIONS = [(280, -40), (280, -20), (280, 0), (280, 20), (280, 40)]
PADDLE_DISTANCE = 50

class Paddles:
    def __init__(self):
        self.left_paddle_body = []
        self.right_paddle_body = []
        self.create_left_paddle()
        self.create_right_paddle()

    def create_left_paddle(self):
        for element in LEFT_PADDLE_POSITIONS:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.setposition(element)
            self.left_paddle_body.append(new_square)

    def create_right_paddle(self):
        for element in RIGHT_PADDLE_POSITIONS:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.setposition(element)
            self.right_paddle_body.append(new_square)

    def move_right_paddle(self, direction):
        for square in self.right_paddle_body:
            square.setheading(direction)
            square.forward(PADDLE_DISTANCE)

    def right_up(self):
        self.move_right_paddle(90)

    def right_down(self):
        self.move_right_paddle(270)

    def move_left_paddle(self, direction):
        for square in self.left_paddle_body:
            square.setheading(direction)
            square.forward(PADDLE_DISTANCE)

    def left_up(self):
        self.move_left_paddle(90)

    def left_down(self):
        self.move_left_paddle(270)



