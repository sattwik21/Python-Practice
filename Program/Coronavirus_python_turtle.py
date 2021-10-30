from turtle import Screen, Turtle
"""
This imports the screen and turtle from the turtle module
"""
from random import randint, choice
"""
This is to use the random integer function and the random choosing of the infected
"""
from time import sleep
posessed = 0
class Person(Turtle):
    population = []

    def __init__(self):
        super().__init__(shape='circle')

        self.shapesize(0.4)
        self.penup()
        self.setpos(randint(-250, 250), randint(-250, 250))

        Person.population.append(self)

    @classmethod
    def all_infected(cls):
        return [person for person in cls.population if person.infected()]

    def infect(self):
        self.color('red')

    def infected(self):
        return self.pencolor() == 'red'
    def all_infected(cls):
        return [person for person in cls.population if person.posessed()]

    def posess(self):
        self.color('yellow')

    def posessed(self):
        return self.pencolor() == 'yellow'


    def random_move(self):
        self.right(randint(-180,180))
        self.forward(randint(0,10))
        if not (-250 < self.xcor() <250 and -250 < self.ycor() < 250):
            self.undo() # this will undo forward()

def make_population(amount):

    for _ in range(amount):
        Person()

def posess_random():
    person = choice(Person.population)
    person.posess()
    posessed+1

def infect_random():
    person = choice(Person.population)
    person.infect()

def simulation():
    """ This will simulate the virus outbreak scenarios (quarantine, or not quarantine) """
    amount=int(input("Enter amount of people within the area: " ))
    moves=int(input("Enter the amount of moves these people will do: "))
    print("Entered amount of people: ", amount)
    print("Entered amount of movements: ", moves)
    make_population(amount)

    infect_random()
    posess_random()

    screen.update()
    for _ in range(moves):
        for person.infected in Person.population:
            person.random_move()

            if not person.infected():
                for infected in Person.all_infected():
                    if person.distance(infected) < 30:
                        person.infect()
                        #this is used to set distance to get infected. In this case I did 30

        screen.update()
        sleep(0.1)


screen = Screen()
screen.setup(500,500)
screen.tracer(0)
screen.bgcolor(str(input("Enter desired background color: ")))
simulation()

screen.exitonclick()
               #this should do it