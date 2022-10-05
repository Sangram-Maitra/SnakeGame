from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_segments(STARTING_POS[i])

    def add_segments(self, POS):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(POS)
        # self.shape("square")
        # self.penup()
        # self.color("white")
        # self.goto(POS)
        self.segments.append(new_segment)

    def extend_seg(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for index in range(len(self.segments)-1, 0, -1):
            new_x_pos = self.segments[index-1].xcor()
            new_y_pos = self.segments[index-1].ycor()
            self.segments[index].goto(new_x_pos, new_y_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def game_reset(self):
        self.clear()
        self.create_snake()

