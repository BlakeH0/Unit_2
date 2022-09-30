# Text Monster Adventure
# Blake Harrington 2022

#Dungeon Map




reset = True
while reset:
    floor_1 = ['empty', 'sword', 'stairs up', 'monster', 'sword']
    floor_2 = ['magic stones', 'sword', 'stairs down', 'monster', 'stairs up']
    floor_3 = ['prize', 'boss monster', 'monster', 'sword', 'stairs down' ]

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
            print("You have found the prize!")#Grab prize + Riddles
            Movement = input("What would you like to do: left, right, up, down, grab, fight, inventory, drop, quit? ")
            if Movement == 'grab':
                    print("You must complete a puzzle in order to pick up the prize!")
                    puzzle_type = input("Would type of puzzle would you like to complete: word, riddle, math, or none?")
                    if puzzle_type == 'word':
                        print("You must try to decipher this word message! You have 2 tries!")
                        print("oyu arleby tbae atth sobs nsoretm utb i  ludwo ldyefintei lpudpaa uoy fi ouy nca burleanscm sith sgeamse!")
                        answer = input("Unscrambled message: ")
                        if answer == "you barely beat the boss monster but i would definitely applaud you if you can unscramble this message!":
                            inventory.append(current_floor[current_room])
                            print("You picked up the prize and won the game! I'll admit, I'm proud of you for persisting!")#User Wins
                            reset = False
                            break
                        else:
                            print("Uh oh! Last chance, try again!")
                            print("You must try to decipher this word message! You have 1 more!")
                            print("oyu arleby tbae atth sobs nsoretm utb i  ludwo ldyefintei lpudpaa uoy fi ouy nca burleanscm sith sgeamse!")
                            answer = input("Unscrambled message: ")
                            if answer == "you barely beat the boss monster but i would definitely applaud you if you can unscramble this message!":
                                inventory.append(current_floor[current_room])
                                print("You picked up the prize and won the game! I'll admit, I'm proud of you for persisting!")#User Wins
                                reset = False
                                break
                            else:
                                print("You did not solve the riddle! You were impaled by spike trap, and died.")
                    elif puzzle_type == 'riddle':
                        print("A girl has as many brothers as sisters, but each brother has only half as many brothers as sisters. How many brothers and sisters are there in the family? ")
                        answer = input("Answer here (NO CAPITALS OR PUNCTUATION/PLEASE CHECK FOR TYPOS): ")
                        if answer == "four sisters and three brothers" or '4 sisters and 3 brothers'  or '3 brothers and 4 sisters' or "three brothers and four sisters":
                            print("You picked up the prize and won the game! I'll admit, I'm proud of you for persisting!")#User Wins
                            reset = False
                            break
                    elif puzzle_type == 'math':
                        print("Solve the for d in the following equation!")
                        print("764(86d+730)=6733896")
                        answer = input("Answer here: ")
                        if answer == '94' or 'd = 94' or 'd=94' or '94=d' or '94 = d':
                            print("Congratulations! You have obtained the prize and won the game!")
                            reset = False
                            break
                        else:
                            print("Nope! You were decapitated by a flying disc trap for answering incorrectly, goodbye!")
                            play_again = input("Do you want to play again y/n? ")
                            if play_again == 'y':
                                print("Okay, good luck!")
                                playing = False
                            elif play_again == 'n':
                                print("Wow, won't even try again? See ya I guess...")
                                reset = False
                                break
                            else:
                                print("You must answer with 'y' or 'n'! ")
                    elif puzzle_type == 'none':
                        print("okay...")
                        print("You were shot in the neck by a poison dart! I told you that you had to solve a puzzle!")
                        play_again = input("Do you want to play again y/n? ")
                        if play_again == 'y':
                            print("Okay, good luck!")
                            playing = False
                        elif play_again == 'n':
                            print("Wow, won't even try again? See ya I guess...")
                            reset = False
                            break
                        else:
                            print("You must answer with 'y' or 'n'! ")

                    else:
                        print("That is not a valid choice! ")#CHECK THIS
        
    #Player Choice
    #Give User A Choice: Left, Right, Up, Down, Grab, Fight, inventory
        Movement = input("What would you like to do: left, right, up, down, grab, fight, inventory, drop, quit? ")
        print('')
        if Movement == 'right' :
            if current_floor != floor_3:#User Can Only Run Away From Monster By Running The Way They Came
                if 'monster' in(current_floor[current_room]):
                    if Movement == 'right':
                        print('You treid to run past the monster? Explains why you died...')
                        play_again = input("Do you want to play again y/n? ")
                        if play_again == 'y':
                            print("Okay, good luck!")
                            playing = False
                        elif play_again == 'n':
                            print("Wow, won't even try again? See ya I guess...")
                            reset = False
                            break
                        else:
                            print("You must answer with 'y' or 'n'! ")
                    elif Movement == 'left' and 'monster' in(current_floor[current_room]):
                        print("You narrowly escaped the monster!")
            if  current_room < 4:#Move Right/Change Room
                current_room += 1
            else:
                print('You cannot go any further in that direction! ')
        elif Movement == 'left' :#Move Left/Change Room
            if current_floor == floor_3:
                if 'monster' in(current_floor[current_room]):
                    if Movement == 'left':
                        print("I cant believe you thought that would be a good idea! Now you're dead so... Great job!!!")
                        play_again = input("Do you want to play again y/n? ")
                        if play_again == 'y':
                            print("Okay, good luck!")
                            playing = False
                        elif play_again == 'n':
                            print("Wow, won't even try again? See ya I guess...")
                            reset = False
                            break
                        else:
                            print("You must answer with 'y' or 'n'! ")
                    elif Movement == 'right' and 'boss monster' in(current_floor[current_room]):
                        print("Good job! You escaped the boss monster by running away!")
                    elif Movement == "right" and 'monster' in(current_floor[current_room]):
                        print("You hardly escaped the monster, good job!")
            if current_room > 0:
                current_room -= 1
            else:
                print('You cannot go any further in that direction! ')
        elif Movement == 'grab':
            if 'sword' in(current_floor[current_room]):#Grab Function
                inventory.append(current_floor[current_room])
                current_floor[current_room] = 'empty'
            elif 'magic stones' in(current_floor[current_room]):#Grab Function
                inventory.append(current_floor[current_room])
                current_floor[current_room] = 'empty'
            elif len(inventory) == 3:#Max Inv
                print("You can only carry three items in your inventory!")
            elif "empty" in(current_floor[current_room]):
                print("You wanna grab something? You are standing in an EMPTY ROOM")
            elif "stairs up"in(current_floor[current_room]):
                print("You really thought you could pick up stairs?")
            elif "stairs down" in(current_floor[current_room]):
                print("You really thought you could pick up stairs?")
            elif "monster" in(current_floor[current_room]):
                print("Yeahhhh just go ahead and put the monster in your pocket!")
                print("You died because you tried to pick up the monster? Interesting...")
                play_again = input("Do you want to play again y/n? ")
                if play_again == 'y':
                    print("Okay, good luck!")
                    playing = False
                elif play_again == 'n':
                    print("Wow, won't even try again? See ya I guess...")
                    reset = False
                    break
                else:
                    print("You must answer with 'y' or 'n'! ")
        elif Movement == 'up':
            if  'stairs up'in(current_floor[current_room]):#Go Upstairs
                floor += 1
                current_floor = floor_level[floor]
            else:#No Stairs At Player Position
                print('You cannot go any further in that direction! ')
        elif Movement == 'down':
            if 'stairs down'in(current_floor[current_room]):#Go Downstairs
                floor -= 1 
                current_floor = floor_level[floor]
            else:#No Stairs At Player Position
                print('You cannot go any further in that direction! ')
        elif Movement == 'fight':
            if 'monster'in(current_floor[current_room]) :
                if 'sword' in(inventory):
                    current_floor[current_room] = 'empty'
                    print("You eradicated the beast, but at the expense of your sword! :(")
                    inventory.remove('sword')
                elif 'sword' not in(inventory):
                    print("You courageously tried to fight the beast, but your effort was of no avail.\n"
                    "Here lies: someone who thought their FISTS would defeat a monster -_-") 
                    play_again = input("Would you like to play again y/n? ")
                    if play_again == 'y':
                        playing = False
                    elif play_again == 'n':
                        print("Whatever I didn't wanna see you die again anyways.")
                        reset = False
                        break
            elif "boss monster"in(current_floor[current_room]):
                if "sword" and 'magic stones' in(inventory):
                    print("You defeated the great boss monster!")
                elif 'sword' or 'magic stones' not in(current_floor[current_room]):
                    print("You tried to fight the boss monster, but you were quickly massacred.\n" 
                    "You must have the magic stones AND the sword to defeat him.")
                    play_again = input("Would you like to try again y/n? ")
                    if play_again == 'y':
                        print("Alright, hopefully you get it this time.")
                        playing = False
                    elif play_again == 'n':
                        print("I guess this is just too hard for you huh?")
                        reset = False
                        break
            else:
                print("Wait... are you gonna fight yourself or something?")
        elif Movement == 'inventory':
            print(f"Your current inventory is: {inventory}")
        elif Movement == 'quit':
            quit = input("Are you sure you want to quit? (y/n) ")#Quit
            print('')
            if quit == 'y':
                reset = False
                break
            elif quit == 'n':
                print("Okay, carry on!")
            else:
                print("You must answer with 'y' or 'n'!")
        elif Movement == 'drop':
            if 'empty' in(current_floor[current_room]):
                drop_item = input("What item in your inventory would you like to drop? ")
                if drop_item in(inventory):
                    if  'empty' in(current_floor[current_room]):
                        (inventory.remove(drop_item))
                        (current_floor[current_room]) = drop_item
                        #replace current room with dropped item
                    else:
                        print("You must be in an empty room to drop something!")
                else:
                    print("That is not an item in your inventory!")
            else: 
                print("The room must be empty for you to drop an item!")
        else:
            print("That is not a valid movement choice!")
        
        





        

