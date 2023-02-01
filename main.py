from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def turtle_race():
    is_race_on = False

    # ---------- BET ----------
    user_bet = screen.textinput(title="Make your bet", prompt="Choose a color to bet on. \n green: Tanjiro \n "
                                                              "pink: Nezuko \n yellow: Zenitsu \n blue: Inosuke \n "
                                                              "red: Rengoku \n black: Muzan").lower()

    # user_bet = screen.textinput(title="Make your bet", prompt="Choose a color to bet on. \n green: Timmy \n "
    #                                                           "pink: Jerry \n yellow: Bob \n blue: Thomas \n "
    #                                                           "red: Sam \n black: Harry").lower()

    if user_bet == "green":
        user_turtle = "Tanjiro"
    elif user_bet == "pink":
        user_turtle = "Nezuko"
    elif user_bet == "yellow":
        user_turtle = "Zenitsu"
    elif user_bet == "blue":
        user_turtle = "Inosuke"
    elif user_bet == "red":
        user_turtle = "Rengoku"
    elif user_bet == "black":
        user_turtle = "Muzan"
    else:
        print("Invalid input. Please try again")
        screen.clear()
        turtle_race()

    # if user_bet == "green":
    #     user_turtle = "Timmy"
    # elif user_bet == "pink":
    #     user_turtle = "Jerry"
    # elif user_bet == "yellow":
    #     user_turtle = "Bob"
    # elif user_bet == "blue":
    #     user_turtle = "Thomas"
    # elif user_bet == "red":
    #     user_turtle = "Sam"
    # elif user_bet == "black":
    #     user_turtle = "Harry"
    # else:
    #     print("Invalid input. Please try again")
    #     screen.clear()
    #     turtle_race()

    # ---------- TURTLES ----------

    colors = ["green", "pink", "yellow", "blue", "red", "black"]
    names = ["Tanjiro", "Nezuko", "Zenitsu", "Inosuke", "Rengoku", "Muzan"]
    # names = ["Timmy", "Jerry", "Bob", "Thomas", "Sam", "Harry"]
    all_turtles = []
    x = -200
    y = 140

    for turtle_index in range(0, 6):
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.goto(x=x, y=y)
        y -= 55
        turtle.color(colors[turtle_index])
        turtle.write(f"{names[turtle_index]}", False, align="center")
        turtle.name = names[turtle_index]
        all_turtles.append(turtle)

    # ---------- RACE ----------

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 200:
                winning_color = turtle.pencolor()
                turtle.write("WINNER", False, align="left")
                if winning_color == user_bet:
                    print(f"You've won! {turtle.name} is the winner!")
                else:
                    print(f"Sorry, {user_turtle} lost. {turtle.name} is the winner.")
                is_race_on = False
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


play_again = True

while play_again == True:
    turtle_race()
    another_game = screen.textinput(title="Turtle Race", prompt="Do you want to play again?").lower()
    if another_game == "no":
        play_again = False
        screen.exitonclick()
    else:
        screen.clear()
        play_again = True
