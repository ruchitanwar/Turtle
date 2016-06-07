import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("blue")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("pink")
	brad.speed(2)
	draw_art(brad)
	brad.right(90)
	brad.forward(200)
	brad.backward(100)
	brad.right(310)
	brad.forward(180)
	u()
	
def u():
	amy = turtle.Turtle()
	amy.shape("arrow")
	amy.color("pink")
	amy.speed(2)
	amy.penup()
	amy.forward(150)
	#amy.left(40)
	amy.pendown()
	amy.forward(100)
	#amy.left(90)
	#amy.forward(200)
	amy.right(90)
	amy.forward(200)
	amy.backward(200)
	amy.left(90)
	amy.forward(100)
	amy.right(90)
	window.exitonclick()




	

def draw_art(brad):
	for each_line in range(0,4):
		brad.forward(100)
		brad.right(90)

draw_square()
draw_line()
