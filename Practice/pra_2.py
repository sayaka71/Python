# 2021.06.11
# Janken

import random

class Janken:

    # set player name
    def __init__(self, your_name="Hiyoko"):
        self.your_name = your_name

    # play janken
    def play(self):

        # player
        try:
            you = int(input("Choose your janken number\n1.Guu\n2.Choki\n3.Par\nInput number: "))
        except ValueError:
            print("Please write number.")

        # computer
        com = random.randint(1,3)

        # judge
        j = you-com
        janken_dic = {1:"Guu", 2:"Choki", 3:"Par"}

        if j==-1 or j==2:
            result = "Win"
        elif j==0:
            result = "Drow"
        else:
            result = "Lose"

        print("{0}: {1}\nComputer: {2}\n{0} {3}!!".format(self.your_name, janken_dic[you], janken_dic[com], result))

jan = Janken()
jan.play()