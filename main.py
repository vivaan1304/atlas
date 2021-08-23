import random
import string
import time

import countries

lst = countries.country


def get_valid_input(prompt, choices, prompt2):
    while True:
        x = input(prompt).lower()
        if x in choices:
            return x
        else:
            print_pause(prompt2)


def print_pause(s):
    print(s)
    t = 2
    time.sleep(t)


def play_again():
    response = get_valid_input(
        "Would you like to play another game(y/n)?\n",
        ["y", "n"],
        "please enter either y or n",
    )
    if response == "y":
        return 1
    else:
        print_pause("Alright!\nThanks for Playing")
        return 0


def wrong_country():
    print_pause("This does not seem correct.\n")


def bad(s, ch):
    if len(s) < 1 or s[0] != ch:
        return -1
    for coun in lst:
        splitted = coun.split(" ")
        for g in splitted:
            if s in g or s == coun:
                return coun
    return -1


def countries_from_char(ch):
    tmp = []
    for coun in lst:
        if coun[0] == ch:
            tmp.append(coun)
    return tmp


def your_turn(ch):
    if len(countries_from_char(ch)) == 0:
        print_pause(
            "There are no more countries(which i know of)" " from this letter"
        )
        print_pause("GAME OVER")
        print_pause("You lose!\n")
        x = play_again()
        if x:
            who_starts()
        else:
            return None
    while True:
        c = input(
            f"Alright! Its your turn, enter a country starting from "
            f"the letter {ch}\n"
            "Enter abort if you want to quit the game\n").lower()
        if "abort" in c:
            print_pause("ABORTED!")
            x = play_again()
            if x:
                who_starts()
                return None
            else:
                return None
        to_rem = bad(c, ch)
        if to_rem == -1:
            wrong_country()
        else:
            print_pause(f"ok, your country is {to_rem}\n")
            lst.remove(to_rem)
            break
    game(1, to_rem[-1])


def game(player, ch):
    if player == 0:
        your_turn(ch)
    else:
        my_turn(ch)


def who_starts():
    print_pause("lets flip a coin to decide who starts the game.")
    inp = get_valid_input(
        "choose heads or tails(h/t).\n",
        ["h", "t"],
        "please enter heads or tails(h/t)",
    )
    flip = random.choice(["h", "t"])
    time.sleep(2)
    print_pause(f"and its.... {flip}")
    ch = random.choice(string.ascii_letters).lower()
    print_pause(f"the starting letter is : {ch}\n")
    if inp == flip:
        print_pause("You start the game!")
        game(0, ch)
    else:
        print_pause("I start the game!")
        game(1, ch)


def my_turn(ch):

    print_pause(
        f"Alright! Its my turn to enter a country "
        f"starting from the letter {ch}"
    )
    tmp = countries_from_char(ch)
    if len(tmp) == 0:
        print_pause(
            "ughh i cant think of any countries starting from this letter"
        )
        print_pause("GAME OVER")
        print_pause("You win!\n")
        return None
    my_country = random.choice(tmp)
    lst.remove(my_country)
    my_country = my_country.title()
    print_pause(f"my country is {my_country}\n")
    game(0, my_country[-1])


def intro():
    print_pause("Hi welcome to atlas: the game\n")
    print_pause("The rules of the game are:")
    print_pause(
        "1. One player starts, they have to type"
        " a country starting from a random letter"
    )
    print_pause(
        "2. The other player has to enter a country starting"
        " from the last letter "
        "of the previous country. For example if the first player says "
        "Armenia the other player has to name a country starting from "
        "the last letter of Armenia i.e. a"
    )
    print_pause(
        "3.The player who is unable to name a country loses\n" "So lets start!"
    )


intro()
who_starts()
