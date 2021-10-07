# Dice Rolling Simulator
import random
import time
from yaspin import yaspin
from yaspin.spinners import Spinners

dice_input = input("Would you like to roll the dice ")
if dice_input == "Yes":
    with yaspin(Spinners.aesthetic):
        time.sleep(5)

    dice_value = random.randint(1,6)
    print(f'Your dice value is...{dice_value} ')
elif dice_input == "No":
    print("Alright see you next time! ")
    exit()
