import random
min_val = 1
max_val = 6

print("Rolling The Dices...")
print("The Value is :")
print(random.randint(min_val, max_val))

roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    roll_again = input("Roll the Dices Again?")
    print(random.randint(min_val, max_val))