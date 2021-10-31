import turtle, time, random
# import explanation:
# turtle    - draws on the screen and makes our racers
# time      - sleep function used before and after race
# random    - this will simulate dice rolls

# make the canvas for our turtles to race on
canvas = turtle.getscreen()

# make player 1's turtle
p1 = turtle.Turtle()
p1.color("red")
p1.shape("turtle")
p1.penup()
p1.goto(-200, 100)
p1.pendown()

# make player 2's turtle
p2 = p1.clone()
p2.color("blue")
p2.penup()
p2.goto(-200, -100)
p2.pendown()

# make the finish line
finish = turtle.Turtle()
finish.pensize(25)
finish.penup()
finish.goto(300, 150)
finish.pendown()
finish.goto(300, -150)
finish.penup()

# give players time to pick their turtle
print("Choose your racer!")
time.sleep(5)

# keep rolling the dice and moving the racers until one finishes
while p1.pos() < (300, 150) and p2.pos() < (300, -150):
    die_roll = random.randint(1, 6)
    print(f"Player 1 rolls {die_roll}")
    p1.forward(die_roll)
    die_roll = random.randint(1, 6)
    print(f"Player 2 rolls {die_roll}")
    p2.forward(die_roll)

# p1 won the race
if p1.pos() >= (300, 150):
    p1.circle(50)
    p1.circle(50)
    p1.circle(50)
    print("Player 1 wins!")
# p2 won the race
elif p2.pos() >= (300, -150):
    p2.circle(50)
    p2.circle(50)
    p2.circle(50)
    print("Player 2 wins!")

# delay the window so players can see results
time.sleep(5)    