import random
import turtle as t
race_on = False
s = t.Screen()
s.setup(width=500,height=400)
user_bet = s.textinput(title="Make your bet",prompt="Choose your Turtle!! Enter a color:")
colors = ['Red','Green','Blue','Black', 'Brown','Orange']
y = [-100,-60,-20,20,60,100]
all_turtles = []
for i in range(6):
    tim = t.Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230,y=y[i])
    tim.color(colors[i])
    all_turtles.append(tim)
if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('you have won')
            else:
                print('you lose!',winning_color,' is the winner')
        dis = random.randint(0,10)
        turtle.forward(dis)
def move_frwrd(d):
    speed = random.randint(10, 100)


s.exitonclick()
