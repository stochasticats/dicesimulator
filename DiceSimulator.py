from random import randint

class Dice:

    def __init__(self):
        self.number = 0
        self.numrolls = 0

    def roll(self):
        self.number = randint(1,6)
        self.numrolls += 1

    def print_state(self):
        if self.numrolls == 0:
            print("You haven't rolled yet!")
        else:
            print("You rolled a {}. \nYou have rolled {} times.".format(self.number, self.numrolls))

if __name__ == '__main__':

    dice = Dice()
    run_sim = True
    print("Welcome to Dice Simulator!")
    while run_sim:
        action = input("Press [R] to roll the dice, [S] to print state, or [X] to exit.").upper()
        if action not in "RSX" or len(action) != 1:
            print("I do not follow, please specify action.")
            continue
        if action == "R":
            dice.roll()
            dice.print_state()
        elif action == "S":
            dice.print_state()
        elif action == "X":
            print("Thanks for playing!")
            run_sim = False

