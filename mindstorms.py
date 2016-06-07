import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("blue")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("pink")
	brad.speed(10)
	for i in range(1,37):
		draw_art(brad)
		brad.right(10)

def draw_art(brad):
	for each_line in range(0,4):
		brad.forward(100)
		brad.right(90)
	
#def draw_circle():	
#	angie = turtle.Turtle()
#	angie.color("red")
#	angie.shape("arrow")
#	angie.circle(100)
#def draw_triangle():	
#	amy = turtle.Turtle()
#	amy.color("green")
#	amy.shape("arrow")
#	for each_line in range(0,3):
#		amy.forward(200)
#		amy.left(120)
			
	

draw_square()
#draw_circle()
#raw_triangle()
window.exitonclick()
