print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
LR=input('You are at a cross road. Where do you want to go? \n Type "Left" or "Right" \n').lower()
if LR=="right":
    print("Game over! You fell into a pit.")

elif LR=="left":
    Wait_swim=input('You have come to a lake. There is an island in the middle.\n Type "wait" to wait for the boat. '
                     'Type "swim" to swim across.\n')
    if Wait_swim=="wait":
        RYG=input("You arrived at the island unharmed. There is a house with three doors.\nOne Red, one Yellow and "
                  "one Blue. Which colour do you choose?\n").lower()
        if RYG=="yellow":
            print("Congratulations...You found the treasure...You won!!")
        elif RYG=="red":
            print("It's a room full of fire...Game Over!")
        elif RYG=="blue":
            print("Room full with water... Game Over!")
    else:
        print("You got encountered by crocodiles... Game over!!")
