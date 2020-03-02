#   Chapter 7
#   CST-186/Winter 2020
#   by Michael Clinesmith

import random # allows use of random numbers
import pickle, shelve # allows use of pickle and shelve to read and write to files

#   Project 7 includes the following updates:
#   More code factored into functions
#   Added more comments explaining functions
#   Implemented Tycoon and Pianist, Gamer and Master Gamer achievements
#   Implemented Merchant appraising
#   Implemented playing Super Mario
#   Implemented playing music
#   Implemented saving and loading files (to include version control)
#   Wheel of Tokens puzzles are now saved in a text file

#   Project 6 includes the following updates:
#   Code organized into functions to provide abstraction and encapsulation
#       making the code easier to read.
#   That was most of the changes.
#   Implemented merchant buying
#   Created merchant buying and selling lists
#   Implemented seller, spender and artist achievements
#   Adjusted looking at shinies and items menu option

#   Project 5 includes the following updates:
#   Creation of dictionaries to hold the description and values of items and description of achievements
#   Creation of additional items
#   Creation of achievements
#   Option to create items
#   Additional menu items - crafting room, dragon merchant, and viewing items
#   Inventory converted from tuples to lists 

#   Project 4 includes the following main updates:
#   Wheel of tokens game added which included significant programming including using for and
#       while loops, selections, and error checking
#   Items may now be added to the inventory
#   Looking at shinies now includes listing the inventory

#   Significant changes in Project 3
#   Creates an introduction image
#   Creates a menu for the user to choose options that repeats until the user chooses to quit
#   Upon completion of a menu selection, a random chance for a user to find an item
#   A number guessing game has been added
#   A token indicator has been added also with looking at your stash.



#   Project 2 code put into a project2 function
#   This function gives the user the option to which programming challenge
#   the user wants to run
#   Selection 2 concatenates 2 strings
#   Selection 3 calculates 15% and 20% tips
#   Selection 4 does some additional math in calculating a final price of a car
#       after adding in extra taxes and fees
#
#   I figured this assignment was easy enough I could do all 3 challenges. ;)

############################################################################################
#   main is the main driver of the program.  It handles the main menu options then calls other
#       functions that handle those options
#   inputs:
#       tokens int: the number of tokens the player has
#       inventory list: the player's inventory
def main():
    global tokens
    global inventory
    again = True
    introMessage()
    while again:
        print(
        """
    Make a selection from the following options:
    1 - Run Project 2 program
    2 - Run Guess Your Number program
    3 - Run Wheel of Tokens program
    4 - Look at your shinies and items
    5 - Crafting - create and interact with items
    6 - Visit dragon merchant
    7 - View achievements
    8 - Load/Save Game
    Q - Exit program
        """
            )
        print ("You have", tokens, "tokens")
        response = input("What is your selection? ")
        if response=="1":  #project2
            project2()
            #possibly add a random item to the inventory
            inventory += getRandomItem()
            checkHoarder(inventory)
        elif response=="2": # number guessing game
            project3NumberGame()
            #possibly add a random item to the inventory
            inventory += getRandomItem()
            checkHoarder(inventory)
        elif response=="3":  #wheel of tokens
            project4WheelOfTokens()
            #possibly add a random item to the inventory
            inventory += getRandomItem()
            checkHoarder(inventory)       
        elif response=="4":  #look at shinies
            viewStashAndInventory(tokens, inventory)
        elif response=="5": #create items
            useInventory(inventory)
        elif response=="6": #purchase or sell items
            visitMerchant(inventory)
        elif response=="7": #view achievements
            viewAchievements()
        elif response=="8":
            loadSaveOption()
        elif response.upper()=="Q":  #quit
            again = False
            print ("Goodbye!")

        else:
            print("Unknown response - choose an option from 1 to 8 and press enter")
        #end of response if

    input ("Press enter to exit the program")  
#end main

def project2():
    #   code to get selection from user
    print(
    """
    Type the number for the program challenge to select, then press enter.
    2 - Favorite Foods
    3 - Tipper Program
    4 - Car Salesman
    """
    )

    selection = input("Enter selection: ")

    if selection == "2": # Favorite Foods Selection
        project2Foods()    
    elif selection == "3": # Tipper Program Selection
        project2Tipper()       
    elif selection == "4": # Car Salesman Selection
        project2CarSales()
    else:
        print("You chose an invalid option.")
    
    input ("Press enter to continue.")
#end project2

#   function inplements the Favorite Foods Project in project 2
def project2Foods():
    print(
            """
    You chose the Favorite Foods Program.
    This program will ask you for two foods you like and combine them.
            """
            )
    food1 = input("Enter your first favorite food: ")
    food2 = input("Enter your second favorite food: ")
    print("\nIf you like " + food1 + " and you like " + food2 + \
              ",\nyou should really like " + (food1 + food2)) 
#end project2Foods

#   function implements the Tipper Program in project 2
def project2Tipper():
    print(
            """
    You chose the Tipper Program.
    This program will ask you for your restaurant bill, then calculate
    a 15% and 20% tip.
            """
            )
    bill = input("Enter the amount of the bill: ")
    bill = float(bill)
    tip15 = bill * .15
    tip20 = bill * .2
    # rounds values  to 2 decimal places
    bill = int(bill*100) / 100
    tip15 = int(tip15*100) / 100
    tip20 = int(tip20*100) / 100
    
    print("When your bill is $" + str(bill) + ",\n"      \
              + "a 15% tip is $" + str(tip15) + ", and\n"    \
              + "a 20% tip is $" + str(tip20) + ".")
#end project2Tipper

#   function implements the Car Salesman Program in Project 2
def project2CarSales():
    print(
            """
    You chose the Car Salesman Program.
    This program will ask the user for the base price of car then
    calculate the price after other fees and taxes are added.
            """
        )
    # percentage fees
    salesTax = .06
    licenseFee = .02
    # constant fees
    dealerPrep = 500
    destCharge = 240

    basePrice = input("Enter the base price of the car: ")
    basePrice = float(basePrice)

    # calculate final price
    finalPrice = basePrice
    finalPrice += basePrice * salesTax
    finalPrice += basePrice * licenseFee
    finalPrice += dealerPrep
    finalPrice += destCharge

    # rounds to 2 decimal places
    finalPrice = int(finalPrice * 100) / 100

    print("The base price of the car is $" , basePrice, sep='')
    print("After taxes of ", salesTax*100, "%,", sep = '')
    print("license fee of ", licenseFee*100, "%,", sep = '')
    print("dealer prep fee of $", dealerPrep, ",", sep = '')
    print("and destination charge of $", destCharge, ",", sep = '')
    print("The final cost of the car is $", finalPrice, sep = '')
#end project2CarSales

#   function implements the Number Guessing Game from project 3
def project3NumberGame():
        print (
            """
    Guess Your Number Game!

    Instructions:
    Pick a number between 1 and 10000
    I will attempt to guess your number
    You give me the following feedback:
    Type '-' and enter if I guessed too high
    Type '+' and enter if I guessed too low
    Type '=' and enter if I guessed your number
    Type 'Q' and enter to quit.

    I will keep guessing until I guess your number.
    Let's do this!
            """
            )
        low=1
        high=10000
        guesses=0
        found=False
        wantToQuit = False
        print ("Pick your number between 1 and 10000")
        input ("Press enter when ready.")
        while not found and not wantToQuit: #loop until answer found or quit
            guess = random.randint(low,high)
            ans= input("Is your number "+str(guess)+"? ")
            guesses+=1
            if ans=="=":             
                print("Awesome!  I got your number!")
                print("It took me", guesses, "tries.\nThanks for playing!")
                found = True
            elif ans=="+":
                print("Too low, huh?  Let me try again.")
                low=guess+1  #change lowest guess since not lower
            elif ans=="-":
                print("So I was too high?  I will try again.")
                high=guess-1 #change highest guess since not higher
            elif ans=="Q":
                print("Had enough?  Well then, goodbye!")
                wantToQuit=True
            else:
                print("Sorry, I don't understand your response.")

            if low>high: #user must have changed number if number not yet found
                print("I think you are playing games on me...")
                low=1    #reset low and high and keep guessing
                high=10000
#ends Number game

#   function implements the Wheel of Tokens game from project 4
def project4WheelOfTokens():
        global tokens
        print (
            """
    Wheel of Tokens!

    Instructions:
    Your goal is to guess the phrase I am thinking of.
    The phrase is initially hidden by '-' characters.
    To reveal the phrase, you can spin the wheel and guess consonants,
    or you can buy vowels
    But be careful, when you spin the wheel, or guess incorrectly, you have
    a chance to go bankrupt!
    Solve the puzzle for a chance to win some tokens.
    Have fun!
            """
            )
        #set up variables
        ALL_VOWELS="aeiou"
        ALL_CON="bcdfghjklmnpqrstvwxyz"
##        PUZZLE_PHRASES=("review your quiz results", "expect the unexpected", "lord of the rings",
##                        "dungeons and dragons", "python programming",
##                        "people say nothing is impossible but i do nothing every day",
##                        "to err is human", "to really foul things up requires a computer",
##                        "comment your code", "no experience required")


        # 0S FOR BANKRUPT, 1S FOR TOKENS, OTHERS SCORE VALUES
        WHEEL=(0, 0, 0, 1, 1, 1, 100, 100, 100, 100, 100, 200, 200, 200, 200, 300, 300, 300,
               500, 500, 600, 700, 800, 1000, 2500)

##        writeWheelPuzzlesToFile(PUZZLE_PHRASES)
        PUZZLE_PHRASES = readWheelPuzzlesFromFile()
        #if no puzzles since file did not load properly, return to calling function
        if (not PUZZLE_PHRASES):
            return;

        #get a random puzzle
        currentPuzzle=PUZZLE_PHRASES[random.randrange(len(PUZZLE_PHRASES))] 
        availableVowels=ALL_VOWELS
        availableCon=ALL_CON
        usedLetters = ()
        score=0
        choice=""
        wheelResult=100
        another = True # used to continue puzzle until completed
        letterGuess = ""
        puzzleGuess = ""
        letterCount=0
        earnedTokens=0



        #hide puzzle letters
        hiddenPuzzle=""
        for letter in currentPuzzle:
            if letter==" ":
                hiddenPuzzle+=" "
            else:
                hiddenPuzzle+="-"

        while another:
            print("Puzzle:", hiddenPuzzle)
            print("Score: ", score)
            print("\nPress 's' to spin the wheel, 'b' to buy a vowel, 'g' to guess the puzzle\n",
                  "or 'q' to quit, then press enter")
            choice = input("What do you want to do? ")
            if choice=="s": #spin the wheel and guess a letter
                input("Press enter to spin the wheel")
                wheelResult=WHEEL[random.randrange(len(WHEEL))]
                if wheelResult==0: #bankrupt
                    print("You spun BANKRUPT!  Your score resets to 0.")
                    score = 0
                    input("Press enter to continue")
                else: #continue to guess a letter
                    if wheelResult==1:
                        print("You spun a token!  Each letter will give you one token!")
                    else:
                        print("The score for each letter is", wheelResult)
                    letterGuess=input("Type a consonant and press enter: ")
                    while ( len(letterGuess) !=1 or letterGuess not in ALL_CON): #not a possible letter choice
                        letterGuess=input("Type a consonant and press enter: ")
                    # check for bad choices first,
                    if letterGuess in usedLetters: #recalled letter already chosen
                        print("You already guessed the letter", letterGuess)
                        score = rollWheelOfShame(score, WHEEL)      #roll wheel of shame 
                    #end of letter reuse
                    elif not letterGuess in currentPuzzle: #letter not in puzzle
                        usedLetters += (letterGuess,)
                        print("Unfortunately", letterGuess, "is not in the puzzle.")
                        score = rollWheelOfShame(score, WHEEL)      #roll wheel of shame
                    #end letter not in puzzle
                    else:                                   #letter in puzzle
                        usedLetters += (letterGuess,)
                        letterCount=0  
                        for i in range(len(currentPuzzle)): # search through puzzle for letters
                            if currentPuzzle[i]==letterGuess:
                                letterCount+=1
                                # replace '-' with letter
                                print("\a",) #play bell
                                hiddenPuzzle=hiddenPuzzle[:i]+letterGuess+hiddenPuzzle[i+1:]
                        #end search
                        print("You found", letterCount, letterGuess)
                        if wheelResult==1:
                            print("You gained", letterCount, "tokens!")
                            tokens+=letterCount
                            checkTycoon()
                        else:
                            print("Your score increases by", letterCount*wheelResult, ".")
                            score+=letterCount*wheelResult
                        input("Press enter to continue")
            #end pick consonant
            elif choice=="b":   # buy a vowel
                if score<250:
                    print("Your score is not large enough to buy a vowel")
                else:
                    letterGuess=input("Type a vowel and press enter: ")
                    while (len(letterGuess) !=1 or letterGuess not in ALL_VOWELS):    #not a possible letter choice
                        letterGuess=input("Type a vowel and press enter: ")
                    # check for bad choices first,
                    score-=250
                    if letterGuess in usedLetters:          #recalled letter already chosen
                        print("You already guessed the letter", letterGuess)
                        score = rollWheelOfShame(score, WHEEL)      #roll wheel of shame                                            
                    #end of letter reuse
                    elif not letterGuess in currentPuzzle:  #letter not in puzzle
                        usedLetters += (letterGuess,)
                        print("Unfortunately", letterGuess, "is not in the puzzle.")
                        score = rollWheelOfShame(score, WHEEL)      #roll wheel of shame                                          
                    #end letter not in puzzle
                    else:                                   #letter in puzzle
                        usedLetters += (letterGuess,)
                        letterCount=0  
                        for i in range(len(currentPuzzle)): #search through puzzle for letters
                            if currentPuzzle[i]==letterGuess:
                                letterCount+=1
                                # replace '-' with letter
                                print("\a",)    #play bell
                                hiddenPuzzle=hiddenPuzzle[:i]+letterGuess+hiddenPuzzle[i+1:]
                        #end search
                        print("You found", letterCount, letterGuess)
                        input("Press enter to continue")                                                  
            elif choice=="g":
                puzzleGuess=input("Type in the puzzle in all lowercase letters,\nand press enter: ")
                while not puzzleGuess:          #make sure user enters something
                    puzzleGuess=input("type in the puzzle in all lowercase letters,\nand press enter: ")
                if puzzleGuess==currentPuzzle:  #puzzle guessed correctly
                    print("The puzzle is:", currentPuzzle)
                    tokens += earnedWheelOfTokens(score) #calculate earned tokens and display messages
                    checkTycoon()
                    another=False
                #end correct guess
                else:
                    print("You guessed the puzzle incorrectly!")
                    score = rollWheelOfShame(score, WHEEL)          #roll Wheel of Shame
            # end choice guess the puzzle   
            elif choice=="q":
                print("Goodbye!")
                another=False
#end of Wheel of Tokens

#   function called when Wheel of Shame rolled
#   inputs:
#       score int: the initial score for the round
#       WHEEL tuple: holds values that can be rolled
#   outputs:
#       newScore int: the final value of the score (could be reset to 0)
def rollWheelOfShame(score, WHEEL):
    newScore=score
    input("Press enter to roll the wheel of shame.")
    wheelResult=WHEEL[random.randrange(len(WHEEL))]
    if wheelResult==0:
        print("You rolled a BANKRUPT!  Your score resets to 0.")
        newScore = 0
    else:
        print("Fortunately you did not go bankrput.")
    input("Press enter to continue")
    return newScore
#end rollWheelOfShame

#   function called to determine number of earned tokens from correctly guessing
#       Wheel of Tokens puzzle
#   inputs:
#       score int: the final score for the round
#   outputs:
#       earnedTokens int: the number of tokens earned
def earnedWheelOfTokens(score):
    earnedTokens=0
    print("Congratulations!  You guessed the puzzle correctly!")
    if score<=100: #determine number of tokens based on score
        earnedTokens=1
    elif score<=300:
        earnedTokens=2
    elif score<=1000:
        earnedTokens=4
    elif score<=3000:
        earnedTokens=6
    elif score<=10000:
        earnedTokens=10
    else:
        earnedTokens=20
    #end if
    print("Your score was", score, ", that earns you", earnedTokens, "tokens!")
    print("Thanks for playing!")
    return earnedTokens
#end earnedWheelOfTokens
    
#   function to print Airy's dragon head
#   note - double backslashes needed or funky stuff happens
def printAiryHead():
    print(
        """
                                       _-- ________
                                   ___/ /_/       /
                                 _/  / /  \\       \\
                      __/\______/         /       /
                     /            (O)     \\       \\
                    /___,                 /       /
                    \ '                   \\_______\\
                     \_______________          \\
                                     \\          \\
                                      \\          \\
                                       |         |
                                       |         |
    """
    )
#end printAiryHead
    
#   function displays an introductionary message
def introMessage():
    print("                           Airy's Game Center!")
    printAiryHead()
    input ("Press enter to continue.")
#end introMessage

#   function to get a random item
#   outputs:
#       foundItem list: A list containing items that have been found
def getRandomItem():
    #find an item?
    global tokens
    item = random.randrange(9)
    print ("You notice an object among lines of text.\nYou find...")
    input ("Press enter to continue")
    foundItem = [] # reset foundItem to blank list in case nothing found
    if item==0:
        print("nothing.  You thought you saw something, but it was nothing.",
                "\nHow disappointing!")            
    elif item==1:
        foundItem = ["Delta flier",]
        print("a", foundItem, itemDescDict.get(foundItem[0]))     
        print ("You add", foundItem, "to your inventory")            
    elif item==2:
        foundItem = ["Super Mario 3 cartridge",]
        print("a", foundItem, itemDescDict.get(foundItem[0]))     
        print ("You add", foundItem, "to your inventory")            
    elif item==3:
        foundItem = ["Slice of pizza",]
        print("a", foundItem, itemDescDict.get(foundItem[0]))
        print ("You add", foundItem, "to your inventory")            
    elif item==4:
        print("a token!  This could be valuable someday!")
        tokens += 1
        checkTycoon()
    elif item==5:
        item = random.randint(3,10)
        print("a pile of tokens!  You count them and discover",item,
              "tokens in the pile!")
        tokens += item
        checkTycoon()
    elif item==6:
        foundItem=["Sonata in A, pg " + str(random.randrange(12)+1),]
        print("a", foundItem, itemDescDict.get(foundItem[0]))
        print ("You add", foundItem, "to your inventory")            
    elif item==7:
        foundItem=["Pencil",]
        print("a", foundItem, itemDescDict.get(foundItem[0]))
        print ("You add", foundItem, "to your inventory")            
    elif item==8:
        foundItem=["Piece of paper",]
        print("a", foundItem, itemDescDict.get(foundItem[0]))
        print ("You add", foundItem, "to your inventory")    
    else:
        print("a time paradox!  Whoa!")   # should not occur
    # if an item found, it is added to inventory
    return foundItem
#end getRandomItem

#   function to add the Artist achievement if it is not yet in achievements
def checkArtist():
    if "Artist" not in achievements:
        print("Congratulations!  You attained the Artist achievement!")
        achievements.append("Artist")
        input("Press enter to continue.")
#end checkArtist

#   function to add the Author achievement if it is not yet in achievements
def checkAuthor():
    if "Author" not in achievements:
        print("Congratulations!  You attained the Author achievement!")
        achievements.append("Author")
        input("Press enter to continue.")
#end checkAuthor

#   function to check if the Gamer achievement should be added
def checkGamer():
    global achievements
    if "Gamer" not in achievements:
        print("Congratulations!  You attained the Gamer achievement!")
        input("Press enter to continue.")
        achievements.append("Gamer")
#end checkGamer
        
#   function to check if Hoarder achievement achieved
#   inputs:
#       invList list: A list of inventory items
def checkHoarder(invList):
    global achievements
    # if more than 10 items, add Hoarder achievement if not in achievements
    if len(invList)>10:
        if "Hoarder" not in achievements:
            achievements.append("Hoarder")
            print("Congratulations!  You attained the Hoarder achievement!")
            input("Press enter to continue.")
#end checkHoarder

#   function to check if the Master Gamer achievement should be added
def checkMasterGamer():
    global achievements
    if "Gamer" not in achievements:
        print("Congratulations!  You attained the Master Gamer achievement!")
        input("Press enter to continue.")
        achievements.append("Master Gamer")
#end checkMasterGamer

#   function to check if the Pianist achievement should be added
def checkPianist():
    global achievements
    if "Pianist" not in achievements:
        print("Congratulations!  You attained the Pianist achievement!")
        input("Press enter to continue.")
        achievements.append("Pianist")
#end checkPianist

#   function to check if the Satisfied achievement should be added
def checkSatisfied():
    #check if pizza slices eaten equals 4, add Satisfied achievement 
    global pizzaSlices
    global achievements
    if pizzaSlices==4 and ("Satisfied" not in achievements):
        print("Congratulations!  You attained the Satisfied achievement!")
        input("Press enter to continue.")
        achievements.append("Satisfied")
#end checkSatisfied

#   function to check if the Seller achievement should be added
#   inputs:
#       spent int: The amount of money gained on a sale
def checkSeller(spent):
    #check if gained 20 tokens
    global achievements
    if spent>=20 and ("Seller" not in achievements):
        print("Congratulations!  You attained the Seller achievement!")
        input("Press enter to continue.")
        achievements.append("Seller")
#end checkSeller

#   function to check if the Spender achievement should be added
#   inputs:
#       spent int: The amount of money spent on a purchase
def checkSpender(spent):
    #check if spent 100 tokens
    global achievements
    if spent>=100 and ("Spender" not in achievements):
        print("Congratulations!  You attained the Spender achievement!")
        input("Press enter to continue.")
        achievements.append("Spender")
#end checkSpender

#   function to check if the Tycoon achievement should be added
def checkTycoon():
    #check if over 1000 tokens owned
    global achievements
    global tokens
    if tokens>1000 and ("Tycoon" not in achievements):
        print("Congratulations!  You attained the Tycoon achievement!")
        input("Press enter to continue.")
        achievements.append("Tycoon")
#end checkTycoon


#   function to view inventory or stash
#   inputs:
#       tokens int: The number of tokens the player has
#       inventory list: A list of the player's inventory items
def viewStashAndInventory(tokens, inventory):
    again = True
    while again:
        print("                           Airy's Stash!")
        printAiryHead()

        print("You have", tokens, "tokens and ", len(inventory), "items.")    
        print(
        """
    Make a selection from the following options:
    1 - Admire tokens
    2 - Examine inventory
    3 - Return to main menu
        """
            )
        response = input("What is your selection? ")

        if response=="1":
            viewTokens(tokens)
        elif response=="2":
            viewInventory(inventory)
        elif response=="3":
            again=False
            print("You leave your stash.")
            input("Press enter to continue.")
        else:
            print("Unknown response.")
#end viewStashAndInventory

#   function that displays a pile of tokens based on the number of tokens in inventory
#   inputs:
#       tokens int: The amount of money the player has
def viewTokens(tokens):
        if tokens==0:
            print(
                """
    There is nothing to see.  You have no money.  Sorry.
                """
            )    
        elif tokens==1:
            print(
                """
                                o
    You have a single token in your stash.  Spend it wisely.
                """
            )
        elif tokens<5:
            print(
                """
                                
                                oo
    You only have a few tokens in your stash.
                """
            )
        elif tokens<10:
            print(
                """
                                 o
                                ooo
    You have a tiny pile of tokens in your stash.
                """
            )    
        elif tokens<25:
            print(
                """
                                 oo
                                oooo
    You have a little pile of tokens in your stash.
                """
            )
        elif tokens<50:
            print(
                """
                                  o
                                 ooo
                                ooooo
    You have a small pile of tokens in your stash.
    That is more than a little.
                """
            )
        elif tokens<75:
            print(
                """
                                  o
                                 oooo
                                oooooo
    You have a moderate pile of tokens.  They are beginning to accumulate.
                """
            )
        elif tokens<100:
            print(
                """
                                  oo
                                ooooo
                               ooooooo
    Your pile of tokens is slightly large.
                """
            )
        elif tokens<250:
            print(
                """
                                  ooo
                                oooooo
                               ooooooooo
    Your pile of tokens is large!
                """
            )
        elif tokens<500:
            print(
                """
                                   o 
                                  oooo
                                oooooooo
                              oooooooooooo
    Your pile of tokens is very large!
                """
            )
        elif tokens<750:
            print(
                """
                                   oo 
                                  ooooo
                                ooooooooo
                              ooooooooooooo
    Wow!  Your pile of tokens is huge!
                """
            )
        elif tokens<1000:
            print(
                """
                                   oo 
                                 oooooo
                              ooooooooooo
                            ooooooooooooooo
    Wow!  Your pile of tokens is very huge!
                """
            )
        else:
            print(
                """
                                   oo 
                                ooooooo
                             ooooooooooooo
                          ooooooooooooooooo
    Wow!  That is quite a pile of tokens!
    There should be an achievement for this!
                """
            )
        input("Press enter to continue.")     
#end viewTokens

#   function that displays the items in the inventory and gives a fuller explanation
#   if requested

def viewInventory(inventory):     
    print ("You have the following items in your inventory:")
    again = True
    while again:
        #list items
        for i in range(len(inventory)):
            print(i, "-", inventory[i])
        print("Press a number and enter to view that inventory item,\nor just enter to return to your stash.")
        response=input("Enter a number then press enter to continue. ")
        again=False
        #check if user entered number on list
        for i in range(len(inventory)):
            if response==str(i):
                print("\n", inventory[i], ":", itemDescDict.get(inventory[i], "Unknown Item"), "\n")
                again=True
        #end for
#end viewInventory

#   function that allows the player to use inventory items
#   inputs:
#       inventory list: A list of the player's inventory items
def useInventory(inventory):
    print("You head to your room.")
    craftingAgain = True
    # loop in crafting until user decides to exit
    while craftingAgain:
        craftingResponse = ""
        print(
            """
    What would you like to do?

    1 - Eat a slice of pizza
    2 - Write down some thoughts
    3 - Create a book
    4 - Create a drawing
    5 - Improve your drawing
    6 - Put together your music
    7 - Play some music
    8 - Play some video games
    9 - Exit the room
            """
            )        

        craftingResponse = input("Type the number of you choice and press enter ")
        if craftingResponse=="1":     #eat pizza
            usePizza(inventory)
        elif craftingResponse=="2":   #write down thoughts
            craftThoughts(inventory)
        elif craftingResponse=="3":   #create a book
            craftBook(inventory)    
        elif craftingResponse=="4":   #create drawing
            craftDragonSketch(inventory)
        elif craftingResponse=="5":   #improve drawing
            craftDragonDrawing(inventory)
        elif craftingResponse=="6":   #put together music
            craftMusicBook(inventory)
        elif craftingResponse=="7":   #play piano
            playMusic(inventory)
        elif craftingResponse=="8":   #play video games
            playSuperMario(inventory)                      
        elif craftingResponse=="9":   #exit
            craftingAgain=False
            print("You leave your room")
        #end crafting response 9
        else:
            print("Unknown response - choose an option from 1 to 9 and press enter")
        input("Press enter to continue.")
#end useInventory

#   function that handles the player eating a slice of pizza
#   inputs:
#       inventory list: A list of the player's inventory items
def usePizza(inventory):
    #check if pizza in inventory
    if "Slice of pizza" in inventory:
        global pizzaSlices
        print("You eat a slice of pizza.  Yum!  That was great!")
        inventory.remove("Slice of pizza")
        pizzaSlices += 1
        #check if pizza slices eaten equals 4, add Satisfied achievement 
        checkSatisfied()
    else:
        print("You have no pizza in your inventory.  Disappointing!")
#end usePizza

#   function that handles the player's attempt to create a Paper of thoughts
#   inputs:
#       inventory list: A list of the player's inventory items
def craftThoughts(inventory):
    randomValue=0
    if "Piece of paper" in inventory:
        if "Pencil" in inventory:
            #75% chance of "Paper of rants", 25% chance of "Paper of thoughts"
            randomValue = random.randrange(4)
            if randomValue==3:
                print("You write down some coherent thoughts on your piece of paper!")
                inventory.remove("Piece of paper")
                inventory.append("Paper of thoughts")
            else:
                print("You write down a bunch of aggravations and frustrations that you have in your mind.",
                    "\nIt may not be a great read, but you feel better.")
                inventory.remove("Piece of paper")
                inventory.append("Paper of rants")
            #10% chance to break pencil
            randomValue = random.randrange(10)
            if randomValue==0:
                print("Unfortunately, your pencil broke.")
                inventory.remove("Pencil")
        else:       #no pencil
            print("You don't have a pencil to write down your thoughts.")
    else:           #no paper
        print("You don't have a piece of paper that you can use to write down your thoughts.")     
#end craftThoughts

#   function that handles the player's attempt to create a Book of wisdom
#   inputs:
#       inventory list: A list of the player's inventory items
def craftBook(inventory):
    #count number of paper of thoughts
    paperOfThoughts=0
    for inventoryObject in inventory:
        if inventoryObject=="Paper of thoughts":
            paperOfThoughts +=1
    #end for
    if paperOfThoughts>=5:
        print("You collect your papers of thoughts into a book of wisdom!  Awesome!")
        for i in range(5):   #remove 5 pages of thoughts
            inventory.remove("Paper of thoughts")
        inventory.append("Book of wisdom")         
        checkAuthor()       #add Author achievement if not yet achieved
    else:
        print("You do not have enough pages to make a book.")
#end craftBook

#   function that handles the player's attempt to create a Draon sketch
#   inputs:
#       inventory list: A list of the player's inventory items
def craftDragonSketch(inventory):
    randomValue=0
    if "Piece of paper" in inventory:
        if "Pencil" in inventory:
            #67% chance of "Paper of scribbles", 33% chance of "Dragon sketch"
            randomValue = random.randrange(3)
            if randomValue==2:
                print("You create a rough but passable sketch of a dragon!")
                inventory.remove("Piece of paper")
                inventory.append("Dragon sketch")
            else:
                print("You create a bunch of scribbles on the paper, but it doesn't look like anything.")
                inventory.remove("Piece of paper")
                inventory.append("Paper of scribbles")
            #10% chance to break pencil
            randomValue = random.randrange(10)
            if randomValue==0:
                print("Unfortunately, your pencil broke.")
                inventory.remove("Pencil")
        else:   #no pencil
            print("You don't have a pencil to draw a sketch.")
    else:       #no paper
        print("You don't have a piece of paper that you can use to draw a sketch.")  
#end craftDragonSketch

#   function that handles a player's attempt create a dragon drawing
#   inputs:
#       inventory list: A list of the player's inventory items
def craftDragonDrawing(inventory):
    randomValue=0
    if "Dragon sketch" in inventory:
        if "Pencil" in inventory:
            #50% chance of "Paper of scribbles", 50% chance of "Dragon drawing"
            randomValue = random.randrange(2)
            if randomValue==1:
                print("You create an impressive scene of a dragon viewing sunset on the edge of a cliff!")
                inventory.remove("Dragon sketch")
                inventory.append("Dragon drawing")
                checkArtist()
            else:
                print("You tried to improve the sketch, but you just made a mess of it.")
                inventory.remove("Dragon sketch")
                inventory.append("Paper of scribbles")
            #10% chance to break pencil
            randomValue = random.randrange(10)
            if randomValue==0:
                print("Unfortunately, your pencil broke.")
                inventory.remove("Pencil")
        else:       #no pencil
            print("You don't have a pencil to work on your sketch.")
    else:           #no dragon sketch
        print("You don't have a dragon sketch to improve.")  
#end craftDragonDrawing

#   function that checks if music pages can be combined
#   inputs:
#       inventory list: A list of the player's inventory items
def craftMusicBook(inventory):
    musicPageName = "Sonata in A, pg 0"
    print("You check your inventory for music pages...")
    #check for first movement
    again = True
    while again:        # repeat until all possible complete 1st movements are made
        allFirst=True
        for i in range(1,5):
            musicPageName = "Sonata in A, pg " + str(i)
            if musicPageName not in inventory:
                allFirst=False
        #end for
        if allFirst:
            print("You put together a complete copy of the first movement of ",
                  "\nFranz Schubert's Sonata in A for Pianoforte!")
            input("Press enter to continue.")
            inventory.append("Sonata in A, first movement")
            #remove single pages
            for i in range(1,5):
                musicPageName = "Sonata in A, pg " + str(i)
                inventory.remove(musicPageName)
        else:
            again=False
    #check for second movement
    again = True
    while again:        # repeat until all possible complete 2nd movements are made
        allFirst=True
        for i in range(5,7):
            musicPageName = "Sonata in A, pg " + str(i)
            if musicPageName not in inventory:
                allFirst=False
        #end for
        if allFirst:
            print("You put together a complete copy of the second movement of ",
                  "\nFranz Schubert's Sonata in A for Pianoforte!")
            input("Press enter to continue.")
            inventory.append("Sonata in A, second movement")
            #remove single pages
            for i in range(5,7):
                musicPageName = "Sonata in A, pg " + str(i)
                inventory.remove(musicPageName)
        else:
            again=False
    #check for third movement
    again = True
    while again:        # repeat until all possible complete 3rd movements are made
        allFirst=True
        for i in range(7,13):
            musicPageName = "Sonata in A, pg " + str(i)
            if musicPageName not in inventory:
                allFirst=False
        #end for
        if allFirst:
            print("You put together a complete copy of the third movement of ",
                  "\nFranz Schubert's Sonata in A for Pianoforte!")
            input("Press enter to continue.")
            inventory.append("Sonata in A, third movement")
            #remove single pages
            for i in range(7,13):
                musicPageName = "Sonata in A, pg " + str(i)
                inventory.remove(musicPageName)
        else:
            again=False
    print("You sort through your inventory and have no complete copies of Schubert's movement to combine.")
#   end craftMusicBook

#   function that implements in options menu for buying or selling from the merchant
#   inputs:
#       inventory list: A list of the player's inventory items
def visitMerchant(inventory):
    print("You see a dragon wearing fancy clothes surrounded by a bunch of items.")
    print("The merchant says 'Rawr - greetings!  \nPardon the mess, I am just setting up!'")
    buySellAgain=True
    buySellResponse=0
    while buySellAgain:

        print(
            """
   What would you like to do?

    1 - Buy items
    2 - Sell items
    3 - Appraise items
    4 - Exit
            """
                )
        buySellResponse = input("Type the number of your choice and press enter ")
        if buySellResponse=="1":    #purchase items
            buyFromMerchant(inventory)
        elif buySellResponse=="2":  #sell items
            sellToMerchant(inventory)
        elif buySellResponse=="3":  #appraise items
            appraiseByMerchant(inventory)
        elif buySellResponse=="4":
            print("The merchant says: 'Rawr - Goodbye'")
            buySellAgain=False
        else:
            print("The merchant says: 'I do not understand what you want to do.'")         
#end visitMerchant

#   function that implements buying an item from the merchant
#   inputs:
#       inventory list: A list of the player's inventory items
def buyFromMerchant(inventory):
    global mercantWillSell
    global merchantMarkUp
    global itemValueDict
    global tokens
    buyResponse = "0"
    responseToInt = 0
    print("The merchant says, 'I have these items for sale.'\n'What would you like to buy?")
    merchantNumOfItems = len(merchantWillSell)
    for i in range(merchantNumOfItems):    #list items and prices
        print(i, "-", merchantWillSell[i], ":", itemValueDict.get(merchantWillSell[i], "??")*2)
    print("Q", "-", "Exit this menu")
    print("You have", tokens, "tokens.\n")

    buyResponse = input("Type the number of your choice and press enter ")

    if buyResponse.upper()=="Q":
                print("The merchant says: 'Um, okay.'")
    else:
        #catch if user does not enter valid integer
        try:
            responseToInt = int(buyResponse)
        except ValueError:
            print("The merchant states, 'I do not understand your response.'")
            return # exit function
        if responseToInt<0 or responseToInt>=merchantNumOfItems: #invalid item number
            print("The merchant states, 'That is not a valid item number.'")
        else:
            itemSellPrice = itemValueDict.get(merchantWillSell[responseToInt])*2
            if tokens>=itemSellPrice:   #enough money to purchase item
                tokens -= itemSellPrice
                print("You hand ", itemSellPrice, "tokens to the merchant.")
                print("He says, 'Thank you for your purchase.'")
                print("You add", merchantWillSell[responseToInt], "to your inventory.")
                inventory.append(merchantWillSell[responseToInt])
                checkHoarder(inventory)
                checkSpender(itemSellPrice)

                if merchantWillSell[responseToInt]=="Topaz":         #unlock Ruby
                      if "Ruby" not in merchantWillSell:
                          merchantWillSell.append("Ruby")
                if merchantWillSell[responseToInt]=="French horn":   #unlock Keyboard
                      if "Keyboard" not in merchantWillSell:
                          merchantWillSell.append("Keyboard")
                if merchantWillSell[responseToInt]=="Keyboard":      #unlock Piano
                      if "Piano" not in merchantWillSell:
                          merchantWillSell.append("Piano")
            #end purchaed item
            else:
                print("The merchant says, 'You do not have enough money to purchase", merchantWillSell[responseToInt], ".'")
#end buyFromMerchant          

#   function that handles selling an item to the merchant
#   inputs:
#       inventory list: A list of the player's inventory items
def sellToMerchant(inventory):
    global mercantWillBuy
    global merchantMarkUp
    global itemValueDict
    global tokens
    sellResponse = "0"
    responseToInt = 0
    print("The merchant says, 'What item would you like to sell me?")
    numOfItems = len(inventory)
    for i in range(numOfItems):    #list items and prices
        if inventory[i] in merchantWillBuy:
            print(i, "-", inventory[i], ":", itemValueDict.get(inventory[i], -2)//2)
        else:
            print(i, "-", inventory[i], ":", "refuses to buy.")
    print("Q", "-", "Exit this menu")
    print("You have", tokens, "tokens.\n")

    sellResponse = input("Type the number of your choice and press enter ")

    if sellResponse.upper()=="Q":
                print("The merchant says: 'Um, okay.'")
    else:
        #catch if user does not enter valid integer
        try:
            responseToInt = int(sellResponse)
        except ValueError:
            print("The merchant states, 'I do not understand your response.'")
            return # exit function
        if responseToInt<0 or responseToInt>=numOfItems: #invalid item number
            print("The merchant states, 'That is not a valid item number.'")
        else:
            itemSellPrice = itemValueDict.get(inventory[responseToInt])//2
            tokens += itemSellPrice
            print("The merchant hands you", itemSellPrice, "tokens.")
            print("He says, 'Thank you for your sale.'")
            print("You remove", inventory[responseToInt], "from your inventory.")
            del inventory[responseToInt]
            checkSeller(itemSellPrice)
            checkTycoon()
#end sellToMerchant

#   function that has the merchant value items
#   inputs:
#       inventory list: A list of the player's inventory items
def appraiseByMerchant(inventory):
    global itemValueDict
    response = "0"
    responseToInt = 0
    again = True
    itemValue = 0
    while again:
        print("The merchant says, 'What item would you like me to appraise for you?")
        numOfItems = len(inventory)
        for i in range(numOfItems):    #list items
            print(i, "-", inventory[i])
        print("Q", "-", "Exit this menu")
        print("You have", tokens, "tokens.\n")

        response = input("Type the number of your choice and press enter ")

        if response.upper()=="Q":
            print("The merchant says: 'Um, okay.'")
            again=False
        else:
            #catch if user does not enter valid integer
            try:
                responseToInt = int(response)
            except ValueError:
                print("The merchant states, 'I do not understand your response.'")
                responseToInt = -1
            if responseToInt<0 or responseToInt>=numOfItems: #invalid item number
                print("The merchant states, 'That is not a valid item number.'")
            else:
                itemValue = itemValueDict.get(inventory[responseToInt])
                print("The merchant says, 'That", inventory[responseToInt],
                  "is worth about", itemValue, "tokens.'")
                print("'But that doesn't mean I will buy or sell it for that price.'\n")
#end appraiseByMerchant

#   function that lets the player play an instrument
#   inputs:
#       inventory list: A list of the player's inventory items
def playMusic(inventory):
    instruments = ("French horn", "Keyboard", "Piano")
    pianoMusic = ("Sonata in A, first movement","Sonata in A, second movement", "Sonata in A, third movement")
    instInInv = []
    musicInInv = []
    again=True
    response = "0"
    musResponse = "0"
    # identify instruments in inventory
    for inst in instruments:
        if inst in inventory:
            instInInv.append(inst)

    if len(instInInv)<1:
        print("You whistle a quick tune since you have no instruments in your inventory!")
    else:
        while again:        #loop while playing instruments
            response = getChoice("What would you like to play?", instInInv) #get instrument choice
            if response==None:
                print("You are done making music for the time being.")
                again = False
            else:
                if (response=="French Horn"):
                    print("You toot your own horn.",
                        "\nNow you need to learn some music to play on this!")
                elif(response=="Keyboard") or (response=="Piano"):
                    #identify pieces of music in inventory
                    for music in pianoMusic:
                        if music in inventory:
                            musicInInv.append(inst)                           
                    if len(musicInInv<1):
                        print("You plunk a few keys on the", response,
                              "\nIt would be nice if you had some piano music.")
                    else:
                        musResponse = getChoice("What piece of music would you like to play?", musicInInv)
                        if musResponse==None:
                            print("You decide not to play the", response)
                        else:
                            print("You play", musResponse, "on the", response, ".",
                                  "It sounds alright; you should get better with practice.")
                            checkPianist()                    
#end playMusic                                            

#   function that has asks the user to choose an item from a list
#   It error checks to require the user to either enter a valid choice or quit
#
#   inputs:
#       question String: The question to be asked
#       inv list: The list of possible answers
#   outputs:
#       answer String: The item in the inventory the user selected, or None if the user quit
def getChoice(question, inv):
    again = True
    response="0"
    responseToInt=0
    answer = "0"
    while again:
        print(question)
        for i in range(len(inv)):
            print(i, ":", inv[i])
        print("Q", "-", "Exit this menu")
        response = input("Type the number of your choice and press enter ")
        if response.upper()=="Q":
            print("You did not make a selection.")
            again = False
            answer = None
        else:
            #catch if user does not enter valid integer
            try:
                responseToInt = int(response)
            except ValueError:
                responseToInt = -1
            if responseToInt<0 or responseToInt>=len(inv): #invalid item number
                print("That is not a valid option.")
            else:
                answer = len(responseToInt)
                again = False
    return answer
#end getChoice

#   function that implements being able to play the Super Mario game       
def playSuperMario(inventory):
    global videoGamesPlayed
    global marioScores
    score = 0
    roundScore = 0
    roundRating = 0
    maxLevel = "0"
    alive = True
    if "Super Mario 3 cartridge" not in inventory:
        print("You don't have a game to play")
    elif "Super Nintendo" not in inventory:
        print("You don't have a game system to play games.")
    elif "TV" not in inventory:
        print("You don't have a TV that you can play games on.")
    elif videoGamesPlayed>=pizzaSlices:
        print("You are getting hungry and need to eat before having a",
            "\nmarathon game session.")
    else:
        print("You sit down to play some games!")
        for i in range(8):
            if alive:
                #calculations to give varied score and survivability which improves slightly
                #with more games
                roundScore = random.randrange(10000 + 1000*videoGamesPlayed) + 10000
                roundRating = random.randrange(120 + (2*videoGamesPlayed) - 10*i)
                roundScore = int(roundRating / 100 * roundScore) * 10
                maxLevel = str(i+1)
                if roundRating>99:
                    print("You easily pass level", i+1, "earning a score of", roundScore, "points!")
                    checkGamer()
                elif roundRating>79:
                    print("You pass level", i+1, "with only a little difficulty, earning", roundScore, "points!")
                    checkGamer()
                elif roundRating>49:
                    print("You struggle but eke through level", i+1, "earning", roundScore, "points!")
                    checkGamer()
                elif roundRating>29:
                    print("You tried your best, but lost your lives on level", i+1, "earning", roundScore, "points.")
                    alive=False
                    input("Press enter to continue.")
                else:
                    print("You completely failed on level", i+1, "earning", roundScore, "points.")
                    alive=False
                    input("Press enter to continue.")
                #end if on rating
            score += roundScore
            roundScore=0
            if alive:  
                input("Press enter to continue.")
        #end for on playing game
        if alive:
            print("Congratulations!  You beat the game!")
            checkMasterGamer()
            maxLevel = "*"
        print("You earned a total score of", score, "!")
        videoGamesPlayed +=1
        marioScores.append( (videoGamesPlayed, score, maxLevel))    #record score
#end playSuperMario

#   function that lists the possible achievements and achievements earned
def viewAchievements():
    print("The following achievements are available in the game:")
    #print list of achievements available
    for key in achievementsDict:
        print(key, ":", achievementsDict[key])
    #print player achievements       
    print("\nYou have attained the following achievements:")
    for i in range(len(achievements)):
        print(achievements[i])
    input("Press enter to continue.")

def loadSaveOption():
    again = True
    response = ""
    while again:
        print(
            """
        Load/Save menu
    Which option would you like to do?
    
    1 - Load a game
    2 - Save a game
    3 - Practice loading/saving files
    Q - Return to main menu
            """
                    )
        response = input( "Type your selection then press enter. ")
        if response=="1":
            loadGame()
        elif response=="2":
            saveGame()
        elif response=="3":
            testThis()
        elif response.upper()=="Q":
            print( "You chose to return to the main menu")
            again=False
        else:
            print( "That is not a valid menu choice ")
#end loadSaveOption

def loadGame():
    print("You chose to load a game")
    again=True
    while again:
        fileName = input("Please input a name to load the file or Q to leave this menu ")
        if fileName.upper()=="Q":
            print("You return to the main menu")
            return              #exit method
        if fileName:
            try:
                saveFile = shelve.open(fileName, "r")
                again=False
            except IOError:
                print("That filename cannot be loaded to restore your game.")
            except:
                print("A strange error happened.  Anyway, that file name is no good.")
    #end while
    #load data from file

    vers = saveFile["version"]

    #allows for compatibility with older versions
    try:
        # make variables global so game can load game data as save into memory
        global version
        global tokens
        global inventory
        global achievements
        global marioScores
        global pizzaSlices
        global videoGamesPlayed
        global merchantWillBuy
        global merchantWillSell

        if vers == "0.7":
            version = vers
            tokens = saveFile["tokens"]
            inventory = saveFile["inventory"]
            achievements = saveFile["achievements"]
            marioScores = saveFile["marioScores"]
            pizzaSlices = saveFile["pizzaSlices"]
            videoGamesPlayed = saveFile["videoGamesPlayed"]
            merchantWillBuy = saveFile["merchantWillBuy"]
            merchantWillSell = saveFile["merchantWillSell"]

            print("Game file", fileName, "loaded into memory")
            
        else:
            print("Incompatible verions, game not restored.")
        saveFile.close()
    except KeyError as e:
        print("\nCorrupted Data, game not restored.")    
#end loadGame

def saveGame():
    print("You chose to save a game")
    again=True
    while again:
        fileName = input("Please input a name to save the file or Q to leave this menu ")
        if fileName.upper()=="Q":
            print("You return to the main menu")
            return              #exit method
        if fileName:
            try:
                saveFile = shelve.open(fileName, "n")
                again=False
            except IOError:
                print("That filename cannot be used.")
    #end while
    #save important data to file

    saveFile["version"] = version
    saveFile["tokens"] = tokens
    saveFile["inventory"] = inventory
    saveFile["achievements"] = achievements
    saveFile["marioScores"] = marioScores
    saveFile["pizzaSlices"] = pizzaSlices
    saveFile["videoGamesPlayed"] = videoGamesPlayed
    saveFile["merchantWillBuy"] = merchantWillBuy 
    saveFile["merchantWillSell"] = merchantWillSell
    saveFile.close()
    print("Game file saved to", fileName, ".")
    
#end saveGame        


#   function that writes the Wheel of Tokens phrases to a file
#   inputs:
#       list list: A list containing possible puzzles in Wheel of Tokens
def writeWheelPuzzlesToFile(list):
    textFile=open("WheelPuzzles.txt", "w")
    for puzzle in list:
        textFile.write(puzzle)
        textFile.write("\n")
    textFile.close()

#   function that loads Wheel of Tokens phrases from the file WheelPuzzles.txt
#   outputs:
#       aList list: A list containing possible puzzles in Wheel of Tokens
def readWheelPuzzlesFromFile():
    aList=[]
    try:
        textFile=open("WheelPuzzles.txt", "r")
        aList = textFile.readlines()

        #remove newlines from puzzles
        for i in range(len(aList)):
            puzzle = aList[i]
            aList[i] = puzzle[:(len(puzzle)-1)]
        
    except IOError:
        print("Unfortunately, there files with the puzzles was not found.")
    return aList

#   function that tests reading and writing to a file
def testThis():
        print("Testing writing the item dictionary to a file.")

        global itemDescDict

        invFile = shelve.open("InvInfo.dat", "n")

        invFile["itemDescDict"] = itemDescDict
        invFile.sync()
        invFile.close()

        print("Testing reading the item dictionary to a variable")

        invFile = shelve.open("InvInfo.dat", "r")
        newInv=invFile["itemDescDict"]
        print("Value in newInv:\n", newInv)

        print("Creating text file with information regarding items")
        itemFile = open("item.txt", "w")
        for aItem in itemDescDict:
            itemFile.write(aItem)
            itemFile.write("/")
            itemFile.write(str(itemValueDict[aItem]))
            itemFile.write("/")
            itemFile.write(itemDescDict[aItem])
            itemFile.write("\n")
        itemFile.close()


        print("End testThis")
#end testThis


#   main
# set up initial variables
version = "0.7"
tokens = 0
inventory = []
achievements = []
marioScores = []
pizzaSlices = 0
videoGamesPlayed = 0
merchantMarkUp = 2

# create item description dictionary
itemDescDict = {"Delta flier": "The text on the flier reads: 'Delta College has helped me get closer to my dreams.'",
            "Super Mario 3 cartridge": "An awesome Super Nintendo game.",
            "Super Nintendo": "A gaming system with a controller that people used to play games in the 20th century.",
            "TV": "A big screen that lets you watch movies and play video games.",
            "Slice of pizza": "A piece of pizza with bacon on it.  Yum!",
            "Sonata in A, pg 1": "A page to the first movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 2": "A page to the first movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 3": "A page to the first movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 4": "A page to the first movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 5": "A page to the second movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 6": "A page to the second movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 7": "A page to the third movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 8": "A page to the third movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 9": "A page to the third movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 10": "A page to the third movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 11": "A page to the third movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, pg 12": "A page to the third movement of Franz Schubert's Sonata in A for Pianoforte.",
            "Sonata in A, first movement": "The first movement of Franz Schubert's Sonata in A.  Airy can play this.",
            "Sonata in A, second movement": "The second movement of Franz Schubert's Sonata in A.  Airy can play this.",
            "Sonata in A, third movement": "The third movement of Franz Schubert's Sonata in A.  Airy can play this.",
            "Pencil": "An item used to write with.",
            "Piece of paper": "A blank piece of paper.",
            "French horn": "A metal instrument made of brass with valves used to play music.  One of Airy's favorite instruments.",
            "Keyboard": "A long instrument with 88 keys used to play music.  Airy can play this.",
            "Piano": "A very heavy large instrument with 88 keys used to play music.  One of Airy's favorite instruments.",
            "Paper of scribbles": "A piece of paper filled with scribbles and unidentifiable objects.",
            "Dragon sketch": "A piece of paper with a rough drawing of a dragon on it.",
            "Dragon drawing": "A piece of paper with detailed drawing of a dragon on it.",
            "Paper of rants": "A piece of paper with incoherent thoughts written on it.",
            "Paper of thoughts": "A piece of paper with interesting thoughts written on it.",
            "Book of wisdom": "A book that gives wisdom to the reader.",
            "Dull sword": "A metal sword.  It is not very detailed or sharp.",
            "Topaz": "A yellowish gem stone.  This could be valuable.",
            "Ruby": "A red gem stone.  This could be valuable."} 

# create item value dictionary
itemValueDict = {"Delta flier": 2,
            "Super Mario 3 cartridge": 50,
            "Super Nintendo": 100,
            "TV": 250,
            "Slice of pizza": 6,
            "Sonata in A, pg 1": 4,
            "Sonata in A, pg 2": 4,
            "Sonata in A, pg 3": 4,
            "Sonata in A, pg 4": 4,
            "Sonata in A, pg 5": 4,
            "Sonata in A, pg 6": 4,
            "Sonata in A, pg 7": 4,
            "Sonata in A, pg 8": 4,
            "Sonata in A, pg 9": 4,
            "Sonata in A, pg 10": 4,
            "Sonata in A, pg 11": 4,
            "Sonata in A, pg 12": 4,
            "Sonata in A, first movement": 32,
            "Sonata in A, second movement": 8,
            "Sonata in A, third movement": 48,
            "Pencil": 1,
            "Piece of paper": 1,
            "French horn": 200,
            "Keyboard": 1000,
            "Piano": 100000,
            "Paper of scribbles": 1,
            "Dragon sketch": 5,
            "Dragon drawing": 25,
            "Paper of rants": 1,
            "Paper of thoughts": 6,
            "Book of wisdom": 80,
            "Dull sword": 50,
            "Topaz": 250,
            "Ruby": 350} 

# create achievements dictionary
achievementsDict = {"Artist": "Create a dragon drawing",
        "Author": "Create a book of wisdom",
        "Gamer": "Pass the first round of Super Mario 3",
        "Hoarder": "Collect over 10 items",
        "Master Gamer": "Pass the 8th round of Super Mario 3",
        "Pianist": "Play one of the movements of Franz Schubert's Sonata in A",
        "Satisfied": "Eat 4 slices of pizza",
        "Seller": "Sell an item worth at least 20 tokens",
        "Spender": "Buy an item for at least 100 tokens", 
        "Tycoon": "Collect over 1000 tokens"}

# create list of items merchant is willing to sell
merchantWillSell = ["Delta flier", "Super Mario 3 cartridge", "Super Nintendo", "TV", "Pencil", "Piece of paper",
                    "Slice of pizza", "French horn", "Dull sword", "Topaz"]

# create list of items merchant is willing to buy
merchantWillBuy = ["Delta flier", "Super Mario 3 cartridge", "Super Nintendo", "TV", "Sonata in A, first movement", 
                    "Sonata in A, second movement", "Sonata in A, third movement", "Slice of pizza", "French horn",
                   "Dragon drawing", "Book of wisdom", "Dull sword", "Topaz", "Ruby"]

# calls the main function which drives the program
main()

             

