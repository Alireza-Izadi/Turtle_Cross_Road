from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
        
    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.random_y = random.choice(range(-240, 280))
            new_car.goto(320, new_car.random_y)
            self.all_cars.append(new_car)
    
    
    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)
            
    def add_speed(self):
        self.speed += MOVE_INCREMENT