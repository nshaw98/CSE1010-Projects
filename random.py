# this program asks you to guess a number and matches it to the number received from the num variable. If it is lower than the number in num, is prints too low. IF it is higher, it prints too high. If it the same, it will print correct.

import random

num = random.randint(1, 10)
guess = 0
while guess != num:
        guess = int(input("Guess a number from 1 to 10: "))
        if guess < num:
                print("too low")
        elif guess > num:
                print("too high")
print("correct")
