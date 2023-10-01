import turtle


drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("PYTHON Cizim Oyunu MKYLisans")


turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def turtle_forward():
    turtle_instance.forward(100)

def turtle_left():
    turtle_instance.left(90)

def turtle_right():
    turtle_instance.right(45)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="a")
drawing_board.onkey(fun=turtle_left,key= "z")
drawing_board.onkey(fun=turtle_right,key= "s")
drawing_board.onkey(fun=clear_screen,key= "x")
drawing_board.onkey(fun=turtle_return_home,key= "c")
drawing_board.onkey(fun=turtle_pen_up,key= "d")
drawing_board.onkey(fun=turtle_pen_down,key= "f")

turtle.mainloop()