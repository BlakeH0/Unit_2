# Text Monster Adventure
# Blake Harrington 2022

#Dungeon Map








from operator import inv


floor_1 = ['empty', 'sword', 'stairs up', 'monster', 'empty']
floor_2 = ['stairs up', 'sword', 'stairs down', 'monster', 'magic stones' ]
floor_3 = ['stairs down', 'empty', 'empty', 'boss monster', 'prize' ]

#Variables
floor_level = [floor_1, floor_2, floor_3]
floor = 0
current_floor = floor_1
current_room = 0
inventory = []

#Game Loop
playing = True
while playing: 
    #Update Current Location
    current_location = current_floor[current_room]    
    #Describe Current Location (CHANGE AFTER COMPLETION TO BE MORE INTERESTING)
    if current_location == 'empty':
        print("You are standing in an empty room.")
    elif current_location == 'sword':
        print("You enter a new room and notice a glistening sword!")
    elif current_location == 'stairs up':
        print("You enter a new room and notice a staircase leading up. ")
    elif current_location == 'monster':
        print("You enter a room and notice a monster! ")
    elif current_location == 'stairs down': 
        print("You enter a room and notice a staircase leading down. ")
    elif current_location == 'magic stones':
        print("You enter a room and notice mystical looking stones. ")
    elif current_location == 'boss monster':
        print("You enter a new room and find yourself \n"
        "in front of the biggest monster you've ever seen! ")
    else:
        print("You have found the prize!")
    
#Player Choice
#Give User A Choice: Left, Right, Up, Down, Grab, Fight, inventory
    Movement = input("What would you like to do: left, right, up, down, grab, fight, inventory? ")
    print('')
    if Movement == 'right' :
        if  current_room < 4:
            current_room += 1
        else:
            print('You cannot go any further in that direction! ')
    elif Movement == 'left' :
        if current_room > 0:
            current_room -= 1
        else:
            print('You cannot go any further in that direction! ')
    elif Movement == 'grab':
        if 'sword' or "magic stones" in(current_floor[current_room]):
            inventory.append(current_floor[current_room])
            current_floor[current_room] = 'empty'
        else:
            print("You wanna grab something? You are standing in an EMPTY ROOM!")
    elif Movement == 'up':
        if  'stairs up'in(current_floor[current_room]):
            floor += 1
            current_floor = floor_level[floor]
        else:
            print('You cannot go any further in that direction! ')
    elif Movement == 'down':
        if 'stairs down'in(current_floor[current_room]):
            floor -= 1 
            current_floor = floor_level[floor]
    elif Movement == 'fight':
        if 'monster'in(current_floor[current_room]) :
            if 'sword' in(inventory):
                current_floor[current_room] = 'empty'
                print("You eradicated the beast, but at the expense of your sword! :(")
                inventory.remove('sword')
            elif 'sword' not in(inventory):
                print("You courageously tried to fight the beast, but your effort was of no avail.\n"
                "Here lies: someone who thought their FISTS would defeat a monster -_-") #Work on what happens after death
        elif "boss monster"in(current_floor[current_room]):
            if "sword" and 'magic stones' in(inventory):
                print("You defeated the great boss monster!")
        else:
            print("Wait... are you gonna fight yourself or something?")
    elif Movement == 'inventory':
        print(f"Your current inventory is: {inventory}")




        

