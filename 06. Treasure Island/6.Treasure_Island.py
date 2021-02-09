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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

choice = input(
    '\nYou\'re at a cross road. Where do you want to go? Choose "left" or "right" : ')
if choice == "left":
    swim = input(
        '\nYou came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
        'Type "swim" to swim across : ')
    if swim == 'wait':
        color = input(
            '\nYou arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. '
            'Which color do you choose : ')
        if color == "yellow":
            print("\nYou Win.")
        elif color == "red":
            print("\nBurned by fire. Game over.")
        elif color == "blue":
            print("\nEaten by beasts. Game Over.")
        else:
            print("\nGame Over.")
    else:
        print("\nAttacked by trout. Game Over.")
else:
    print("\nYou fell into a hole. Game Over.")
