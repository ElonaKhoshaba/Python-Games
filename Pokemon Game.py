import random

#####################################USER AND AI####################################

class User(object):
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.attacking_pokemon = None
      
    def set_pokemon(self):
        set_of_pokemon = self.pokemon
        
    def heal(self):
        if self.attacking_pokemon.hp<self.attacking_pokemon.maxhealth:
            if self.attacking_pokemon.hp+20>self.attacking_pokemon.maxhealth:
                self.attacking_pokemon.hp=self.attacking_pokemon.maxhealth
                print("Your pokemon was healed to max health!")
            elif self.attacking_pokemon.hp<self.attacking_pokemon.maxhealth:
                self.attacking_pokemon.hp+=20
                print("Your pokemon was healed to",self.attacking_pokemon.hp)
        else:
            print("Your pokemon was already at max health smh")
            
    def attack(self, attack_name, enemy):
        pattack=True
        pmap=(self.attacking_pokemon.attackdict[attack_name][0]+random.choice(range(((self.attacking_pokemon.attackpower)-20),self.attacking_pokemon.attackpower)))/10
        failure=(self.attacking_pokemon.attackdict[attack_name][1])*10
        rando=random.choice(range(1,10))
        if failure==rando or failure<rando:
            pattack=False
            print("Sorry! Your pokemon missed the attack..!")

        while pattack==True:
            if isinstance(enemy, GrassType) and isinstance(self.attacking_pokemon, FireType):
                specialap=pmap*1.5
                enemy.hp-=specialap
                print("Special hit!",enemy.name,"now has",enemy.hp,"hit points!")
                pattack=False
            elif isinstance(enemy, WaterType) and isinstance(self.attacking_pokemon, GrassType):
                specialap=pmap*1.5
                enemy.hp-=specialap
                print("Special hit!",enemy.name,"now has",enemy.hp,"hit points!")
                pattack=False
            elif isinstance(enemy, FireType) and isinstance(self.attacking_pokemon, WaterType):
                specialap=pmap*1.5
                enemy.hp-=specialap
                print("Special hit!",enemy.name,"now has",enemy.hp,"hit points!")
                pattack=False
            else:
                enemy.hp-=pmap
                print(enemy.name,"now has",enemy.hp,"hit points!")
                pattack=False
        
class Computer(User):
    def set_pokemon(self,lista):
        self.pokemon.append(lista[random.choice([0,1])])
        self.pokemon.append(lista[random.choice([2,3])])
        self.pokemon.append(lista[random.choice([4,5])])
        set_of_pokemon = self.pokemon
        self.attacking_pokemon=self.pokemon[random.choice([0,1,2])]
        print(self.name+"'s starting pokemon is: "+self.attacking_pokemon.name)

    def attack(self, enemy):
        global c_specialap
        cattack=True
        attack_name=random.choice([1,2,3])
        cmap=(self.attacking_pokemon.attackdict[attack_name][0]+random.choice(range(((self.attacking_pokemon.attackpower)-20),self.attacking_pokemon.attackpower)))/10
        accuracy=(self.attacking_pokemon.attackdict[attack_name][1])*10
        crando=random.choice(range(1,10))
        if accuracy==crando or accuracy<crando:
            cattack=False
            print("Your opponent missed the attack!")
            
        while cattack==True:
            if isinstance(enemy, GrassType) and isinstance(self.attacking_pokemon, FireType):
                c_specialap=cmap*1.5
                enemy.hp-=c_specialap
                print("Your opponent achieved a special hit!",enemy.name,"now has",enemy.hp,"hit points")
                cattack=False
            elif isinstance(enemy, WaterType) and isinstance(self.attacking_pokemon, GrassType):
                c_specialap=cmap*1.5
                enemy.hp-=c_specialap
                print("Your opponent achieved a special hit!",enemy.name,"now has",enemy.hp,"hit points")
                cattack=False
            elif isinstance(enemy, FireType) and isinstance(self.attacking_pokemon, WaterType):
                c_specialap=cmap*1.5
                enemy.hp-=c_specialap
                print("Your opponent achieved a special hit!",enemy.name,"now has",enemy.hp,"hit points")
                cattack=False
            else:
                enemy.hp-=cmap
                print(enemy.name,"now has",enemy.hp,"hit points")
                cattack=False
    def switch(self):
        x=True
        switchp=self.pokemon[random.choice([0,1,2])]
        while x==True:
            if switchp!=self.attacking_pokemon and switchp.hp>0:
                self.attacking_pokemon=switchp
                x=False
            elif switchp==self.attacking_pokemon or switchp.hp<=0:
                switchp=self.pokemon[random.choice([0,1,2])]
    
    def heal(self):
        if self.attacking_pokemon.hp<self.attacking_pokemon.maxhealth:
            if self.attacking_pokemon.hp+20>self.attacking_pokemon.maxhealth:
                self.attacking_pokemon.hp=self.attacking_pokemon.maxhealth
                print(self.attacking_pokemon.name,"was healed to max health!")
            elif self.attacking_pokemon.hp<self.attacking_pokemon.maxhealth:
                self.attacking_pokemon.hp+=20
                print(self.attacking_pokemon.name,"pokemon was healed to",self.attacking_pokemon.hp)
        else:
            print(self.attacking_pokemon.name,"pokemon was already at max health smh")
            

###########################POKEMON##########################################################
        
class Pokemon(object):
    def __init__(self, hp, attackpower, name):
        self.hp = hp
        self.maxhealth=hp
        self.attackpower=attackpower
        self.name = name
        self.knocked_out = False
        self.attacks = self.set_attacks()
    
    def __str__(self):
        return(self.name+" has " +str(self.hp) +" hit points and "+ str(self.attackpower) +" attack power ~")

class GrassType(Pokemon):
    def set_type(self):
        return 'grass'
    def set_attacks(self):
        self.attacklist={"Leaf Storm":[130,.9],"Mega Drain":[50,1],"Razor Leaf":[55,.95]}
        self.attackdict={1:[130,.9],2:[50,1],3:[55,.95]}
    def print_attacks(self):
        print(1,": Leaf Storm", self.attacklist["Leaf Storm"], " " , 2, ": Mega Drain,", self.attacklist["Mega Drain"]," ",3, ": Razor Leaf", self.attacklist["Razor Leaf"])

class WaterType(Pokemon):
    def set_type(self):
        return 'water'
    def set_attacks(self):
        self.attacklist={"Bubble":[40,1],"Hydro Pump":[185,.3],"Surf":[70,.9]}
        self.attackdict={1:[40,1,"Bubble"],2:[185,.3,"Hydro Pump"],3:[70,.9,"Surf"]}
    def print_attacks(self):
        print(1,": Bubble", self.attacklist["Bubble"], " " , 2, ": Hydro Pump,", self.attacklist["Hydro Pump"]," ",3, ": Surf", self.attacklist["Surf"])

class FireType(Pokemon):
    def set_type(self):
        return 'fire'
    def set_attacks(self):
        self.attacklist={"Ember":[60,1],"Fire Punch":[85,.8],"Flame Wheel":[70,.9]}
        self.attackdict={1:[60,1,"Ember"],2:[85,.8,"Fire Punch"],3:[70,.9,"Flame Wheel"]}
    def print_attacks(self):
        print(1,": Ember", self.attacklist["Ember"], " " , 2, ": Fire Punch,", self.attacklist["Fire Punch"]," ",3, ": Flame Wheel", self.attacklist["Flame Wheel"])

#########################GAME LOOP####################################################
    
def game_loop():
    p1name=input("What is your name?")
    AI_name=input("What is the name of your (AI) opponent?")
    Player1=User(p1name)
    AI=Computer(AI_name)
    
    
    Bulbasaur=GrassType(160, 40, 'Bulbasaur')
    Bellsprout=GrassType(140, 60, 'Bellsprout')
    Oddish=GrassType(150, 50, 'Oddish')
    Charmander=FireType(125, 70, 'Charmander')
    Ninetails=FireType(130, 50, 'Ninetails')
    Ponyta=FireType(140, 60, 'Ponyta')
    Squirtle=WaterType(180, 20, 'Squirtle')
    Psyduck=WaterType(170, 40, 'Psyduck')
    Polywag=WaterType(150, 50, 'Polywag')

    pokemonlist=[Bulbasaur,Bellsprout,Oddish,Squirtle,Psyduck,Polywag,Charmander,Ninetails,Ponyta]

#choosing pokemon
    print("These are the grass type pokemon.")
    print(Bulbasaur)
    print(Bellsprout)
    print(Oddish)
    x=True
    while x == True:
        pokemon1=input("Please type the pokemon name")
        if pokemon1== "Bulbasaur":
            Player1.pokemon.append(Bulbasaur)
            x= False
            pokemonlist.remove(Bulbasaur)
        elif pokemon1 == "Bellsprout":
            Player1.pokemon.append(Bellsprout)
            x=False
            pokemonlist.remove(Bellsprout)
        elif pokemon1== "Oddish":
            Player1.pokemon.append(Oddish)
            x=False
            pokemonlist.remove(Oddish)
        else:
            print("Invalid choice, try again!")
  

    print("These are the water type pokemon.")
    print(Psyduck)
    print(Polywag)
    print(Squirtle)
    x=True
    while x == True:
        pokemon1=input("Please type the pokemon name")
        if pokemon1== "Psyduck":
            Player1.pokemon.append(Psyduck)
            x= False
            pokemonlist.remove(Psyduck)
        elif pokemon1 == "Squirtle":
            Player1.pokemon.append(Squirtle)
            x=False
            pokemonlist.remove(Squirtle)
        elif pokemon1== "Polywag":
            Player1.pokemon.append(Polywag)
            x=False
            pokemonlist.remove(Polywag)
        else:
            print("Invalid choice, try again!")
            
    print("These are the fire type pokemon.")
    print(Charmander)
    print(Ponyta)
    print(Ninetails)
    x=True
    while x == True:
        pokemon1=input("Please type the pokemon name")
        if pokemon1== "Charmander":
            Player1.pokemon.append(Charmander)
            x= False
            pokemonlist.remove(Charmander)
        elif pokemon1 == "Ponyta":
            Player1.pokemon.append(Ponyta)
            x=False
            pokemonlist.remove(Ponyta)
        elif pokemon1== "Ninetails":
            Player1.pokemon.append(Ninetails)
            x=False
            pokemonlist.remove(Ninetails)
        else:
            print("Invalid choice, try again!")


#Choose first pokemon

    x= True
    while x == True:
        spokemon=input("Pick your starting pokemon (1, 2, 3).")
        if spokemon=="1":
            Player1.attacking_pokemon=Player1.pokemon[0]
            x=False
        elif spokemon == "2":
            Player1.attacking_pokemon=Player1.pokemon[1]
            x=False
        elif spokemon=="3":
            Player1.attacking_pokemon=Player1.pokemon[2]
            x=False    
        else:   
            print("Invalid choice, try again.")
            
    print("Your starting pokemon is: "+Player1.attacking_pokemon.name)
    AI.set_pokemon(pokemonlist)
    print("----------------LET THE BATTLE BEGIN!----------------")
    
#player move
    
    game=True
    turn=0
    while game==True:
        while turn%2==0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~your turn~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            if Player1.attacking_pokemon.hp<=0:
                if Player1.pokemon[0].hp<=0 and Player1.pokemon[1].hp<=0 and Player1.pokemon[2].hp<=0:
                    print("You have no pokemon left to play, you LOSE")
                    game=False
                else:
                    print("Your current pokemon has KOed. You need to swtich")
                    for i in range(3):
                        print(Player1.pokemon[i].name,"has",Player1.pokemon[i].hp,"hit points and",Player1.pokemon[i].attackpower,"attack power.")
                    switchpokemon=input("Pick the pokemon you want to switch to (1, 2, 3)")
                    if switchpokemon=="1":
                        Player1.attacking_pokemon=Player1.pokemon[0]
                        turn+=1
                    elif switchpokemon == "2":
                        Player1.attacking_pokemon=Player1.pokemon[1]
                        turn+=1
                    elif switchpokemon=="3":
                        Player1.attacking_pokemon=Player1.pokemon[2]
                        turn+=1    
                    else:   
                        print("Invalid choice, try again.")
            else:
                pplay=input("Do you want to attack, switch, or heal?")
                if pplay=='attack':
                    print("Here's your arsenal: (listed attack power and accuracy)")
                    eval(Player1.attacking_pokemon.name).print_attacks()
                    pattack=eval(input("Pick your poison (1, 2, 3)"))
                    if pattack==1 or pattack==2 or pattack==3:
                        Player1.attack(pattack, eval(AI.attacking_pokemon.name))
                        turn+=1
                    else:
                        print("Invalid choice, try again")
                        
                elif pplay=='switch':
                    print("As a refresher:")
                    for i in range(3):
                        print(Player1.pokemon[i].name,"has",Player1.pokemon[i].hp,"hit points and",Player1.pokemon[i].attackpower,"attack power.")
                    switchpokemon=input("Pick the pokemon you want to switch to (1, 2, 3)")
                    if switchpokemon=="1":
                        Player1.attacking_pokemon=Player1.pokemon[0]
                        turn+=1
                    elif switchpokemon == "2":
                        Player1.attacking_pokemon=Player1.pokemon[1]
                        turn+=1
                    elif switchpokemon=="3":
                        Player1.attacking_pokemon=Player1.pokemon[2]
                        turn+=1    
                    else:   
                        print("Invalid choice, try again.")

                elif pplay=='heal':
                    print(Player1.heal())
                    turn+=1
            
        while turn%2==1:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~oppenent's turn~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            cplay=random.choice(range(6))
            if AI.attacking_pokemon.hp<=0:
                AI.switch()
                if AI.pokemon[0].hp<=0 and AI.pokemon[1].hp<=0 and AI.pokemon[2].hp<=0:
                    print(AI_name,"has no more pokemon to play, you win!")
                    game=False
            else:
                if cplay>=3:
                    print(AI_name,"chose to attack")
                    AI.attack(eval(Player1.attacking_pokemon.name))
                    turn+=1
                elif cplay==1:
                    print(AI_name,"chose to switch")
                    AI.switch()
                    turn+=1
                elif cplay==2:
                    print(AI_name,"chose to heal")
                    AI.heal()
                    turn+=1
   
            

            
game_loop()
