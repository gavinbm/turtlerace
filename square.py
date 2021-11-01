import turtle, time

# we need a canvas to draw on
canvas = turtle.getscreen()

# make our little turtle guy
buddy = turtle.Turtle()
buddy.color("green")
buddy.shape("turtle")

# draw the square
buddy.forward(100)
buddy.left(90)
buddy.forward(100)
buddy.left(90)
buddy.forward(100)
buddy.left(90)
buddy.forward(100)

# pause so we can see buddy's beautiful artwork
time.sleep(5)