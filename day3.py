'''print("welcome to rollercoster servie")
age=int(input("enter you age plz:-"))
if age>20:
    print("you are allowed to ride coster")
else:
    print("you are not allowed to ride coster")

-----------------------------------------------------------------------

num=10%3
print(num)

num=int(input("enter your number:-"))
if num%2==0:
    print("its even")
else:
    print("its odd")

--------------------------------------------------------------------

print("Welcome to Roller Coaster Service")

height = int(input("Enter your height please: "))
age = int(input("Enter your age please: "))
bill=0

if height > 120:
    print("You are allowed to ride the coaster")

    if age < 12:
        bill=5
        print("You pay $5")
    elif 12 <= age < 80:
        bill=10
        print("You pay $10")
    else:
        bill=15
        print("You pay $15")

    want_photo=input("do you want photo :-y/n")
    if want_photo=="y":
        bill=bill+3
        print(f"your final bill={bill}")

else:
    print("You are not allowed to ride the coaster")


-------------------------------------------------------------

print("welcome to pizza service")
pizza=input("enter your pizza size S,M,L:-")
peproni=input("do you want peproni?Yes/No:-")
cheese=input("do you want cheese?Yes/No:-")
bill=0

if pizza=="S":
    bill=15
elif pizza=="M":
    bill=20
elif pizza=="L":
    bill=25
else:
    print("wrong input")

if peproni=="Yes":
    if pizza=="S":
        bill+=2

    else:
        bill+=3

if cheese=="Yes":
    bill+=1

print(f"your final bill={bill}")

-------------------------------------------------------

height = int(input("Enter your height please: "))
age = int(input("Enter your age please: "))
bill=0

if height > 120:
    print("You are allowed to ride the coaster")

    if age < 12:
        bill=5
        print("You pay $5")
    elif 12 <= age < 80:
        bill=10
        print("You pay $10")

    elif 45 <= age <= 55:
        print("you dont have to pay the bill")
    else:
        bill=15
        print("You pay $15")

    want_photo=input("do you want photo :-y/n")
    if want_photo=="y":
        bill=bill+3
        print(f"your final bill={bill}")

else:
    print("You are not allowed to ride the coaster")

------------------------------------------------------------------------

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake.\n"
                    "Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()

    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed.\n"
                        "There is a house with 3 doors.\n"
                        "One red, one yellow, and one blue.\n"
                        "Which colour do you choose? ").lower()

        if choice3 == "yellow":
            print("🎉 You Win! You found the treasure!")
        elif choice3 == "red":
            print("🔥 Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("🐺 Eaten by beasts. Game Over.")
        else:
            print("🚪 Game Over.")

    else:
        print("🐟 Attacked by trout. Game Over.")

else:
    print("🕳️ Fall into a hole. Game Over.")'''


