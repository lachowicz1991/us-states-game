import turtle
import pandas

image = "blank_states_img.gif"
df = pandas.read_csv('50_states.csv')
print(df)
screen = turtle.Screen()
screen.addshape(image)
turtle.shape(image)
answer_turtle = turtle.Turtle() # create turtle object to display answer
answer_turtle.hideturtle()
all_states = df.state.to_list()
guessed_states = []


def game(x, y):
	answer_user = screen.textinput(title=f'{str(len(guessed_states))}/50 States Correct', prompt="Name the state:")
	state = answer_user.title()

	if state in set(df['state']):
		print('state found')
		state_row = df[df.state == state]  # select row that matches the state
		x_value = state_row['x'].values[0]  # get value of x column for selected row
		y_value = state_row['y'].values[0]  # get value of y column for selected row
		answer_turtle.penup()
		answer_turtle.goto(x_value, y_value)
		answer_turtle.write(state_row.state.item(), align="center", font=("Arial", 12, "normal"))
		guessed_states.append(state)
		print(guessed_states)
	else:
		print("State not found")

while len(guessed_states) < 50:
	turtle.onscreenclick(game)
	turtle.mainloop()