from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT ="center"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("black")
        self.goto(-220, 250)
        self.level = 0
        self.add_level()
    
    def add_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align = ALIGNMENT,font =FONT)
            
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!",  align = ALIGNMENT,font =FONT)