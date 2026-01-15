'''import random

random_int=random.randint(1,10)
num=int(input("enter any number by your mood-"))
if num==random_int:
    print("the number are same")
else:
    print("the number are different")
print(f"the number was{random_int}")
-----------------------------------------------------------------------

import random
print("---rock paper scissors game---")

list1=["rock","paper","scissors"]
random_int=random.choice(list1)

you_choice=input("enter rock paper scissors---").lower()
computer_choice=random_int

if you_choice==computer_choice:
    print("you both put same its tie game")
elif (
    (you_choice == "rock" and computer_choice == "scissors") or
    (you_choice == "paper" and computer_choice == "rock") or
    (you_choice == "scissors" and computer_choice == "paper")
):
        print("you won the game")
elif you_choice in computer_choice:
    print("You lose!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")
print(f"the computer put-{computer_choice} ")'''

