from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.seth(90)
        self.goto(0, -280)
    
    def move_up(self):
        if self.ycor() < 280:
            self.forward(MOVE_DISTANCE)
    
    def move_down(self):
        if self.ycor() > -280:
            self.backward(MOVE_DISTANCE)
            
            
    def reset_position(self):
        self.goto(0, -280)