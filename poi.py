from random import randint
from os import system

def event():
    system("clear")
    x = randint(0, 10)
    note = ""
    if x == 7:
        print("You found a flower")
    elif x%2 == 0:
        print("Fight")
    else:
        print("Nothing of interest")
    return note