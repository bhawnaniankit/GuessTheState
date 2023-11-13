from turtle import Turtle,Screen
import pandas
screen=Screen()
screen.bgpic("./US_State_Games/blank_states_img.gif")

gussed=[]

states=pandas.read_csv("./US_State_Games/50_states.csv")
state_list=states["state"].to_list()

abhay=Turtle()
abhay.color("black")
abhay.hideturtle()
abhay.penup()

user_score=0
while user_score<50:
    user_guess=screen.textinput(title=f"Enter a {user_score+1}/50 state ",prompt="Guess a state")
    if(user_guess.title() in state_list and user_guess not in gussed):
        gussed.append(user_guess)
        user_score+=1
        gussed_state=states[states["state"]==user_guess.title()]
        abhay.goto(int(gussed_state["x"].to_list()[0]),int(gussed_state["y"].to_list()[0]))
        abhay.write(user_guess.title(),True,"center")
screen.exitonclick()