from turtle import Turtle
PADDLE_POSITIONS = ((-350, 0), (350, 0))


class Paddle(Turtle):
    # def __init__(self, position):
    #     super().__init__()
    #     self.paddle = []
    #     self.create_paddle()
    #     self.paddle_a = self.paddle[0]
    #     self.paddle_b = self.paddle[1]
    #
    # def create_paddle(self):
    #     # for position in PADDLE_POSITIONS:
    #     paddle_a = Turtle()
    #     paddle_a.speed(0)
    #     paddle_a.shape('square')
    #     paddle_a.color('white')
    #     paddle_a.penup()
    #     paddle_a.goto(PADDLE_POSITIONS[0])
    #     paddle_a.shapesize(5, 1)
    #     self.paddle.append(paddle_a)
    #
    #     paddle_b = Turtle()
    #     paddle_b.speed(0)
    #     paddle_b.shape('square')
    #     paddle_b.color('white')
    #     paddle_b.penup()
    #     paddle_b.goto(PADDLE_POSITIONS[1])
    #     paddle_b.shapesize(5, 1)
    #     self.paddle.append(paddle_b)
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
