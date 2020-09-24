import random

def gameloop():
    gamestate=True
    print("Welcome to Hangman! After you choose a difficulty,",
          "a word will be chosen at random and you'll have to",
          "guess it letter by letter before you run out of attempts!",
          "You can also guess the whole word but be warned that takes",
          "away two attempts (you only get 10!). Good luck!",sep="\n")
    player_resp=input("What difficulty do you want? (easy, medium, or hard) E/M/H").lower()
    
    
    easy_words = ["funny","dog","cat","pet","grade","letter","bird","fruit","cars","bed","mattress","apple","happy","angry"]
    
    medium_words = ["peach","pineapple","galaxy","elephant","automobile","carrots","bedframe","pillowcase","wagon"]
    
    hard_words = ["juxtaposition","automotive","disregard","ostrich","flapjack","espionage","gnarly","duplex","daiquiri","bandwagon"]

    if player_resp == "e":
        chosen_word = random.choice(easy_words).lower()
    elif player_resp == "m":
        chosen_word = random.choice(medium_words).lower()
    elif player_resp == "h":
        chosen_word = random.choice(hard_words).lower()
        
    while gamestate==True:
            
        player_guess = None # will hold the players guess
        guessed_letters = [] # a list of letters guessed so far
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-") # create an unguessed, blank version of the word
        joined_word = None # joins the words in the list word_guessed

#your points so far:
#youve entered (wrong: a,b,h)
        HANGMAN = (
"""
    
           
               
            
          
                               ____________
     ___                      |   under    |
    |   |______               |construction|
    |          |              |____________|  
    |__________|                    | 
""",
"""
    
           
               
            
          
                               ____________
     ___             o        |   under    |
    |   |______     /|\       |construction|
    |          |     |        |____________|  
    |__________|    / \             | 
""",
"""
    
           
               
            
          
                           ____________
     ___             o   < where am i..|     
    |   |______     /|\   |____________|   
    |          |     |          
    |__________|    / \             
""",
"""
       ____
      |    |      
      |         
      |      
      |    
      |                    ______
     _|_             o   < oh god|
    |   |______     /|\   |______| 
    |          |     |    
    |__________|    / \  
""",
"""
       ____
      |    |    ____________________  
      |    o  < where is my body?   |
      |         this makes it worse |
      |        |____________________| 
      |                    
     _|_               
    |   |______     /|\   
    |          |     |    
    |__________|    / \  
""",
"""
       ____
      |    |      
      |    o      
      |    |    
      |    
      |                    
     _|_               
    |   |______     / \   
    |          |     |    
    |__________|    / \   
""",
"""
       ____
      |    |      
      |    o      
      |    |\     
      |    
      |                    
     _|_               
    |   |______     /   
    |          |     |    
    |__________|    / \  
""",
"""
       ____
      |    |      
      |    o      
      |   /|\    
      |    
      |                    
     _|_               
    |   |______      
    |          |     |    
    |__________|    / \  
""",
"""
       ____
      |    |      
      |    o      
      |   /|\     
      |    |
      |                    
     _|_               
    |   |______       
    |          |        
    |__________|    / \ 
""",
"""
       ____
      |    |      
      |    o      
      |   /|\     
      |    | 
      |   /              
     _|_                  
    |   |______       
    |          |        
    |__________|      \
""",
"""
       ____
      |    |      
      |    o      
      |   /|\     
      |    |
      |   / \                 
     _|_               
    |   |______       
    |          |        
    |__________|  
""")

        print(HANGMAN[0])
        attempts = 10

        while attempts != 0 and "-" in word_guessed:
            print("You have",attempts,"attempts remaining")
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except: # check valid input
                print("That is not valid input. Please try again.")
                continue                
            else: 
                if not player_guess.isalpha(): # check the input is a letter. Also checks an input has been made.
                    print("That is not a letter. Please try again.")
                    continue
                elif len(player_guess) > 1: # check the input is only one letter
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters: # check it letter hasn't been guessed already
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed: # no blanks remaining
            print(("\nCongratulations! {} was the word").format(chosen_word))
        else: # loop must have ended because attempts reached 0
            print(("\nUnlucky! The word was {}.").format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            gamestate = False

gameloop()


