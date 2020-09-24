import random
random40=[2,3,2,3,2] #40% chance of death when player runs
floor1=['nothing','spear','goblin','door','stairs up','nothing','bow']
floor2=['goblin','stairs up','bow','door','stairs down','nothing','goblin'] #FLOOR PLAN
floor3=['spear','stairs down','spear','goblin','door','stairs up','bow']
floor4=['secret path','nothing','spellbook','stairs up','door','stairs down','goblin']
floor5=['a password','spear','nothing','stairs down','nothing','troll','the wizard boss!!']
floors=[floor1,floor2,floor3,floor4,floor5]
user_floor=0
user_room=0
inventory=[] #empty inventory
gamestate=True
move='yes'
dead='no'
print('Welcome to the Python Dungeon. Your mission is to defeat the evIL wizard.')
while gamestate==True:
    move='yes' #dictates whether player can move left or right
    if user_floor<0:
        user_floor=0
    if user_room<0: #states boundaries of dungeon
        print("You've hit the end of the dungeon. That response is invalid.")
        user_room=0
    if user_room>6: 
        print("You've hit the end of the dungeon. That response is invalid.")
        user_room=6
    print('-----------------------------------------------------------------------------')
    print("You're standing on floor",user_floor+1,"in room",user_room+1,", and there is",floors[user_floor][user_room]) #tells player position  
    print('You have:',inventory)
    if floors[user_floor][user_room]=='goblin':
        move='no' #prohibits player from moving when they encounter goblin
        print('There is a goblin! Fight or run!')
    if floors[user_floor][user_room]=='spellbook': 
        print('Hmm.. a spellbook may be useful.')
    if floors[user_floor][user_room]=='door':
        print('The door is locked.. have a key?')
        if 'key' not in inventory:
            move='no' #if player doesn't have key, they can't move through door
        if 'key' in inventory:
            floors[user_floor][user_room]='unlocked door' #changes locked door to unlocked forever
            inventory.remove('key')
            move='yes'
    if floors[user_floor][user_room]=='secret path':
        print("You've stumbled upon a secret path. Go up to take it.") 
    if floors[user_floor][user_room]=='a password':
        print("A sheet of paper says [ORANGE APPLE]... Maybe you should remember this..") #gives player password for boss fight
    if floors[user_floor][user_room]=='troll':
        answer = input("Hello traveler. Give me the password if you want to pass.")
        if answer == 'ORANGE APPLE':
            print("Correct.. you may pass.") #allows player to move if password is correct
            move='yes' 
        else:
            print('Wrong password. Try again.') #kicks player out of room if password is wrong
            user_room-=1
    action=input('What would you like to do - move left/right, go up/down, grab, fight, run, or get help?') #gives player all possible commands
    if action=='get help':
        print('Your possible actions are move left/right, go up/down, grab, fight, run, or get help.')
    if action=='move right':
        if floors[0:][:6] and move=='yes': #sets boundaries for moving right
             user_room+=1
        if move=='no' and floors[user_floor][user_room]=='door':
            user_room-=1
            print('You had no key and left the room.')
        if move=='no' and floors[user_floor][user_room]=='goblin': #traps player in monster rooms
            print("You can't move past a goblin!")
    if action=='move left':
        if floors[0:][1:] and move=='yes': #sets boundaries for moving left
            user_room-=1
        if move=='no' and floors[user_floor][user_room]=='door':
            user_room+=1
            print('You had no key and left the room.')
        if move=='no' and floors[user_floor][user_room]=='goblin': #traps player in monster rooms
            print("You can't move past a goblin!")
    if action=='grab':
        if floors[user_floor][user_room]=='spear' or floors[user_floor][user_room]=='bow' or floors[user_floor][user_room]=='a password' or floors[user_floor][user_room]=='spellbook':
            inventory.append(floors[user_floor][user_room])
            print('Your inventory is now:',inventory)  #adds item to inventory and reports it
            floors[user_floor][user_room]='nothing'
        elif floors[user_floor][user_room]=='nothing' or floors[user_floor][user_room]=='goblin' or floors[user_floor][user_room]=='troll' or floors[user_floor][user_room]=='the wizard boss!!':
            print("Invalid response! There's nothing to grab.")         #negates invalid responses for grab
    if action=='go up':
        if floors[user_floor][user_room]!='stairs up' and floors[user_floor][user_room]!='secret path': 
            print("You can't do that there's no up stairs here smh.")
        if floors[user_floor][user_room]=='stairs up' or floors[user_floor][user_room]=='secret path':
            user_floor+=1 #moves player up a floor at stairs and secret path
    if action=='go down':
        if floors[user_floor][user_room]!='stairs down':
            print("You can't do that there's no down stairs here smh.") #negates for invalid reponse
        if floors[user_floor][user_room]=='stairs down':
            user_floor-=1 #moves player down a floor
    if action=='run':
        if floors[user_floor][user_room]!='goblin':
            print("What are you trying to run from? You can't do that. And you cAN't run from a boss. Try again.")
        if floors[user_floor][user_room]=='goblin':
            if random.choice(random40)==3: #40% chance of running away
                print("You sucessfully ran away! (wimp)")
                user_room-=1
            if random.choice(random40)!=3: #60% chance of dying
                print('You were too slow! You DIED!!')
                dead='yes' 
    if action == 'fight':
        if floors[user_floor][user_room]!='goblin' and floors[user_floor][user_room]!='the wizard boss!!':
            print("What are you trying to fight? No no no, try again.") #negates invalid reponse
        if floors[user_floor][user_room]=='goblin':
            if 'spear' in inventory or 'bow' in inventory:
                weapon=input('Which weapon do you want to use? Bow or spear?')
                if weapon in inventory: #removes weapons after use
                    inventory.remove(weapon)
                    print("You've defeated the goblin! Seems like it dropped a key..")
                    inventory.append('key') #adds keys to inventory after killing goblins
                    print('Your inventory is now',inventory)
                    floors[user_floor][user_room]='nothing'
                elif weapon not in inventory: #kills player for trying to finess game smdh
                    print("You tried to fight with",weapon,"and died!")
                    dead='yes'
            elif 'spear' not in inventory and 'bow' not in inventory:
                print("You tried to fight with your fists and DIED!") #kills player if fighting without weapons
                dead='yes'
        if floors[user_floor][user_room]=='the wizard boss!!':
            if 'spear' in inventory and 'bow' in inventory and 'spellbook' in inventory: #need all three weapons to defeat boss
                print("You've defeated the boss with your bow and spear! He exploded into GOLD! You're rich!! YOU WIN THE GAME!")
                floors[user_floor][user_room]='nothing'
                gamestate='no'
            if 'spear' not in inventory or 'bow' not in inventory or 'spellbook' not in inventory:
                print("You tried to fight with",[inventory],"and DIED") #kills player if not all three weapons in inventory
                dead='yes'
    if dead=='yes': #stops game if player died
        gamestate=False
while gamestate==False:
    print("GAME OVER... You've failed. Quit to play again.") #prints end message and stops game
    gamestate='no'

