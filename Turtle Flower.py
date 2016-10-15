from random import random
import turtle

window = turtle.Screen()
window.bgcolor("black")

def draw_leaf(turtle):
    base = turtle.pos()
    turtle.circle(100,75)
    turtle.goto(base)
    turtle.circle(-100,75)
    turtle.goto(base)

def draw_art(turtle):
    turtle.right(90)
    turtle.forward(400)
    turtle.left(62)
    draw_leaf(turtle)
    leaves = 0
    while leaves < 6:
        turtle.left(27)
        draw_leaf(turtle)
        leaves = leaves + 1
    turtle.ht()
    
charlie = turtle.Turtle()
charlie.shape("turtle")
charlie.color("Green", "SeaGreen")

draw_art(charlie)
draw_leaf(charlie)

def draw_triangle(turtle_name, radius):
    turtle_name.circle(radius,360,3)

def draw_square(turtle_name, radius):
    turtle_name.circle(radius,360,4)


class TurtleArtist(turtle.Turtle):
    _origin = (0, 0)
    _starts = []
    _level = 1
    _len = 100

        
    def mark_future_start(self):
        self._starts.append(self.position())

    def clear_all_starts(self):
        self._starts = []
        print('Added a new Start')
        print(self._starts)

    def incrememnt_level(self):
        self._level += 1

    def to_origin(self):
        try:
            if self._origin:
                self.goto(self._origin)
        except AttributeError:
                self.home()

    def triangle(self, ang_step1, ang_step2):
        self.turn_move(ang_step1)
        self.mark_future_start()
        self.turn_move(ang_step2)
        self.to_origin()

    def turn_move(self, angle_dist):
        """Pass in (ang, dist) for turtle to turn and move """
        self.right(angle_dist[0])
        self.forward(angle_dist[1])

    def style(self, color='#009b30', shape='turtle', speed=0.1, pen=(0, 0, 0)):
        self.color(color)
        self.pencolor(pen[0], pen[1], pen[2])
        self.shape(shape)
        self.speed(speed)

    def flower(self, orig_angle1, orig_angle2):
        self._origin = self.position()
        for x in range(1, 25):
            self.triangle(orig_angle1, orig_angle2)

    def make_stem(self):
        pensize = self.pensize()
        self.pencolor('#238c13')
        self.pensize(6)
        self.setheading(270)
        self._starts.append(casey.position())
        self.forward(460)
        self.penup()
        self.to_origin()
        self.pendown()
        # Return pensize to however it was before method was called
        self.pensize(pensize)

    def run_through_levels(self):
        length = self._len
        if self._level > 2:
            print('time to end')
            return True
        for start in self._starts:
            self._starts = self._starts[1:]
            if len(self._starts) < 3 and self._level == 2:
                length = 3
            self.penup()
            self.goto(start)
            self.pendown()
            for i in range(1, 2):
                mod = length * i ** 0.9
                casey.flower((0, mod), (18, 40))
                casey.flower((0, mod), (-18, 40))

            self.pencolor((random(), random(), random()))
            self.incrememnt_level()
            # self._len *= 0.2
            self._len = 10
            self.run_through_levels()


window = turtle.Screen()

casey = TurtleArtist()
casey.goto(0, 100)
casey.pensize(1.1)
casey.shape('turtle')
casey.speed(500)
casey.make_stem()
casey.pencolor('#FBE54E')
casey.run_through_levels()



window.exitonclick()



