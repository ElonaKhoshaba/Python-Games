board=[1,2,3,4,5,6,7,8,9]
moves=[] #stores played spaces
Px=input("P1, what's your name?") #defining variables
Po=input("P2, what's your name?") #player names 
game=True
turn='x'
counter=0
def winner(): #checks for every possible win
    global game 
    if board[0:3]==['x','x','x'] or board[0::4]==['x','x','x'] or board[0::3]==['x','x','x'] or board[1::3]==['x','x','x'] or board[2::3]==['x','x','x'] or board[2:8:2]==['x','x','x']:
        game=False
        print(Px,"has won the game!")       
    elif board[0:3]==['o','o','o'] or board[0::4]==['o','o','o'] or board[0::3]==['o','o','o'] or board[1::3]==['o','o','o'] or board[2::3]==['o','o','o'] or board[2:8:2]==['o','o','o']:
        game=False
        print(Po,"has won the game!")        
    else:
        tie()

def tie(): #checks for tie if more than 9 moves
    global game
    if counter==9:
        print("It's a tie!")
        game=False
        
def checker(): #checks moves for already played numbers, doesnt allow 
    global move
    if move in moves:
        return False
    else:
        return True
    
def boardd(): #prints board
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

while game==True: 
    if turn=='x': #x turn
        winner()
        if game==True: #double checks to avoid 1/2 loop at end
            move=int(input(Px+ " what is your move (1-9)?"))
            if checker()==True:
                board[move-1]='x'
                moves.append(move)
                boardd()
                counter+=1
                turn='o'
            else:
                print("You can't go there smh")
                turn='x'
    if turn=='o': #o turn
        winner()
        if game==True: #double checks to avoid 1/2 loop at end
            move=int(input(Po+ " what is your move (1-9)?"))
            if checker()==True:
                board[move-1]='o' #changes # to letter
                moves.append(move)
                boardd()
                counter+=1
                turn='x'
            else:
                print("You can't go there smh")
                turn='o'
        

  
    




