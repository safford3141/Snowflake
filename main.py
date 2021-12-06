import turtle

bg = turtle.Screen()
bg.tracer(0)
bg.bgcolor('black')

flake = turtle.Turtle()
flake.speed(0)
flake.color('Grey')
flake.fillcolor('White')
flake.width(3)
flake.ht()
flake.pu()
flake.setpos(0,200)
flake.pd()


flake2 = turtle.Turtle()
flake2.speed(0)
flake2.width(3)
flake2.color('Grey')
flake2.fillcolor('White')
flake2.ht()
flake2.pu()
flake2.setpos(-50,200)
flake2.pd()


def flake_c():
	flake.begin_fill()
	flake.circle(50,360,5)
	flake.end_fill()

	flake2.begin_fill()
	flake2.circle(50,360,5)
	flake2.end_fill()



for i in range(10000):
	flake.clear()
	flake.setheading(i*.2)

	flake2.clear()
	flake2.setheading(i*.2)

	
	flake_c()

	flake.setheading(-90)
	flake.forward(.2)

	flake2.setheading(-90)
	flake2.forward(.2)
	

	bg.update()

bg.update()

