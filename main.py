import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("Indian State Quiz")
img = r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\day-25-start\india-state.gif"
screen.addshape(img)
turtle.shape(img)
data = pd.read_csv(r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\day-25-start\states_data.csv")
all_states = data["state"].to_list()
guessed_states = []
score = 0
while len(guessed_states) < 29:
    answer = screen.textinput(title=f"Your Score is : {score}/29", prompt="What's another state name ?").title()
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states) 
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(r"C:\Users\SHIVAM SINHG\Desktop\100DaysofCode\day-25-start\missing_states.csv")
        print("You have exited the game.")
        break
    if answer in all_states:
        guessed_states.append(answer)
        score += 1
        print("Correct guess!")
        print(f"Your score is {score}")
        t1 = turtle.Turtle()
        t1.hideturtle()
        t1.penup()
        state_data = data[data.state == answer]
        t1.goto(state_data.x.item(), state_data.y.item())
        t1.write(answer)
turtle.mainloop()