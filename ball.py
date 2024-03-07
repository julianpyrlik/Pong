from turtle import Turtle
import random
import paddles
SPEED_INCREASE = 1
STARTING_SPEED = 6
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.starting_speed = STARTING_SPEED

    def move(self):
        self.forward(self.starting_speed)

    def set_start_heading(self):
        self.setposition(0, 0)
        starting_list = ["left", "right"]
        who_starts = random.choice(starting_list)
        if who_starts == "left":
            self.setheading(random.randint(150, 210))
        elif who_starts == "right":
            self.setheading(random.randint(-30, 30))

    def wall_collision(self):
        if self.ycor() > 245 or self.ycor() < -245:
            self.setheading(360 - self.heading())  # Angle of incidence = angle of reflection

    def bounce_back_right(self,right_paddle):
        # Right Paddle
        if self.xcor() >= 255 and self.distance(right_paddle[2]) < 60:  # edge is reached and distance to paddle[3] is small # Ball is higher
            difference_right = self.ycor() - right_paddle[2].ycor()
            self.setheading(180 - difference_right)
            self.starting_speed += SPEED_INCREASE

    def bounce_back_left(self,left_paddle):
        # Left Paddle
        if self.xcor() <= -265 and self.distance(left_paddle[2]) < 60:  # edge is reached and distance to paddle[3] is small # Ball is higher
            difference_left = self.ycor() - left_paddle[2].ycor()
            self.setheading(0 + difference_left)
            self.starting_speed += SPEED_INCREASE

    def speed_back_to_normal(self):
        self.starting_speed = STARTING_SPEED

