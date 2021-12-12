
# Guessing game
import random

n = random.randrange(1, 100)
i = 0
print("Guess the number in range of 1 to 100")
while i < 10:
    if i < 9:
        print("You have", 10 - i, "attempts left")
    elif i == 9:
        print("This is your last attempt, be careful")
    ui = int(input("Please guess the number\n"))
    i = i + 1
    if ui > n and i < 10:
        print("your number is greater than actual number\n")
        continue
    elif ui < n and i < 10:
        print("your number is lower than actual number\n")
        continue
    elif ui == n:
        print("Congratulation you are correct\n", "You have guessed in", i, "th attempt")
        break
    elif ui != n and i == 10:
        print("Game Over")
print("Thank you\n", "The correct number is ", n)