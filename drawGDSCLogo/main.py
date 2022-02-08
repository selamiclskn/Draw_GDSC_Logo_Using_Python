
import turtle

pencil=turtle.Turtle()
pencil.screen.bgcolor("black") # set background color black
pencil.shape("turtle") # set icon shape

def draw_shape(start_x,start_y):
    """
    function for lines
    start_x: x coordinate to start the line
    start_y: y coordinate to start the line
    """
    pencil.penup()
    pencil.goto(start_x,start_y)
    pencil.pendown()
    pencil.begin_fill()
    pencil.circle(25,180)
    pencil.forward(125)
    pencil.circle(25,180)
    pencil.forward(125)
    pencil.end_fill()

pencil.color("#ea4335") # red line
pencil.right(150)
draw_shape(-200,0)

pencil.color("#4286f4") # blue line
pencil.right(60)
draw_shape(-176,0)

pencil.color("#fbbd04") # yellow line
pencil.right(120)
draw_shape(125,-45)

pencil.color("#0f9d58") # green line
pencil.right(60)
draw_shape(101,-45)

# text
pencil.penup()
pencil.goto(0,-220)
pencil.pendown()
pencil.color('white')
style = ('Courier', 30, 'bold')
pencil.write('Google Developer Student Club\n\t@gdscinonu',
             font=style,
             align='center')

pencil.hideturtle()
turtle.done()
#author : selamiclskn
