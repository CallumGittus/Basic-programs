from random import randint #Imports random integer function into this program.
battleshipGrid = [] #This defines an empty array list.

print("-------------------------------------------------------------------") #prints top heading banner.
print("----------------------WELCOME TO BATTLESHIPS-----------------------") #prints top heading banner.
print("-------------------------------------------------------------------\n") #prints top heading banner.

while True: #start of a while true loop.    
    player1=str(input("Player one, please enter your name: "))#player 1 inputs their name.
    if player1.isalpha(): #validation for characters from the alphabet only.
        # Do something with valid input.
        break #This ends the loop.
    else: #this defines the response for any other answer than the correct input earlier in the loop.
        print("Invalid input, please try again!\n") #this is data validation, users are asked to re-enter the input  
while True: #start of a while true loop.
    player2=str(input("Player two, please enter your name: "))#player 2 inputs their name.
    if player2.isalpha(): #validation for characters from the alphabet only.
        # Do something with valid input.
        break #This ends the loop.
    else: #this defines the response for any other answer than the correct input earlier in the loop.
        print("Invalid input, please try again!\n") #this prints the response for any invalid inputs 

player1Wins = (0) #tracks player 1s wins.

player2Wins = (0) #tracks player 2s wins.

def createGrid(grid): #This defines the function for creating the 6*6 grid 
    for item in range(6): #for loop that continues to run until there are 6 "O" values in the list 
        grid.append(["O"] * 6) #adds "O" for each item in the grid

def displayGrid(grid): #defines function for showing the grid
    for row in grid: #for loop that creates the grid 
        print(" ".join(row)) #prints the grid 

def startGame(grid): #defines the function that starts the game with the welcome message and also places the location of the battleship
    del grid[:] #deletes and previous grid, acts as a refresh
    print("\nThe aim of the game is to sink the battleship before your opponent!") #prints output message
    print("First to destroy 3 ships wins! \n") #prints output message
    createGrid(grid) #calls on creategrid function to create the grid
    displayGrid(grid) #calls on displaygrid function to display the grid 
    global gridCol #uses variable outside of the function
    gridCol = randint(1, len(grid)) #picks a random column for the battleship location
    global gridRow #uses variable outside of the function
    gridRow = randint(1, len(grid[0])) #picks a random row for the battleship location
    print("\nAnswers: \nrow" , gridRow) #DELETE for testing purposes
    print("col" , gridCol, "\n") #DELETE for testing purposes
    
    return { #turns the result from grid column and grid row back to the caller
        'gridCol': gridCol, #returns gridCol value to gridCol 
        'gridRow': gridRow, #returns gridRow value to gridRow 
    }


def playAgain(): #defines play again function 
    userInput = input("Do you want to play again? Enter yes or no: ").lower() #asks for user input to restart or exit game
    if userInput == ("yes"): #if statement for when user types "yes"
        global player1Wins #allows the function to call from variables outside function
        player1Wins = 0 #resets player1Wins variable to 0
        global player2Wins #allows the function to call from variables outside function
        player2Wins = 0 #resets player2Wins variable to 0
        coordinates = startGame(battleshipGrid) #Function is called upon to start the game 
        player1Input() #calls upon player1input() function 
    elif userInput == ("no"): #else if statement for when user inputs "no"
        print("Thanks for playing") #prints a statement
        exit() #exits the program
    else: #else statement
        print("Invalid input, Please try again") #prints a statement 
        playAgain() #calls upon the play again function 


def playerWins(): #defines playerwins function
    if player1Wins == (3): #if statement for when player wins are equal to 3
        print(player1 , " wins!\n") #prints a statement to say that player1 wins
        playAgain() #calls upon playagain function
    elif player2Wins == (3): #if statement for when player wins are equal to 3
        print(player2 , " wins\n")#prints a statement to say that player2 wins
        playAgain() #calls upon playagain function
    else: #else statement 
       player1Input() #calls on player1input() function


def player1Input(): #defines player1input function
   global player1InputRow #calls from variable outside the function
   global player1InputCol #calls from variable outside the function
   global player1Wins #calls from variable outside the function
   while True: #begins while true loop
      try: #try statement that executes the code below 
         print("\n" + player1 + ", your turn to guess!") #prints the players name and tells them its their turn
         player1InputRow = int(input(player1 + ", Enter the row: ")) #input that asks player 1 for their row guess
         player1InputCol = int(input(player1 + ", Enter the coloumn: ")) #input that asks player 1 for their col guess
      except ValueError: # data validation for entering integers into previous inputs for column and row
            print("Please enter a number.") #prints a statement
            continue #goes back to the beginning of loop 
      else: #else statement
         break #stops loop 
   if player1InputRow == gridRow and player1InputCol == gridCol: #if statement to check for correct answers 
      print("\nCongratulations " + player1 + ", you've destroyed the battleship!\n") #prints a statement telling player 1 they have sunk the battleship
      del player1InputRow #deletes player 1s input for row
      del player1InputCol #deletes player 1s input for col
      player1Wins += 1 #adds 1 to player 1s wins 
      print(player1 , "has " , player1Wins ," wins") #prints how many wins player 1 has
      print(player2 , "has " , player2Wins ," wins") #prints how many wins player 2 has
      coordinates = startGame(battleshipGrid)#Function is called upon to start the game
      playerWins() #calls on playerWins function
   elif player1InputRow > 6 or player1InputRow < 1 and player1InputCol > 6 or player1InputCol < 1: #else if statement for when inputs are not between 1 and 6
      print("Enter a number between 1 and 6") #prints a message that tells user to enter a number between 1 and 6
      player1Input() #calls on player 1 input function
   else: #else statement
      print("Better luck next time!") #prints a statement for when answer is wrong
      player2Input() #calls on player 2 input function

def player2Input(): #defines player2input function
   global player2InputRow #calls from variable outside the function
   global player2InputCol #calls from variable outside the function
   global player2Wins #calls from variable outside the function
   while True:#begins while true loop
      try: #try statement that executes the code below 
         print("\n" + player2 + ", your turn to guess!") #prints the players name and tells them its their turn
         player2InputRow = int(input(player2 + ", Enter the row: ")) #input that asks player 2 for their row guess
         player2InputCol = int(input(player2 + ", Enter the coloumn: ")) #input that asks player 2 for their col guess
      except ValueError: # data validation for entering integers into previous inputs for column and row
            print("Please enter a number.") #prints a statement telling player to enter a number
            continue #goes back to the beginning of loop 
      else: #else statement
         break #stops loop 
   if player2InputRow == gridRow and player2InputCol == gridCol: #if statement to check for correct answers 
      print("\nCongratulations "  , player2 , ", you've destroyed the battleship!\n") #prints a statement telling player 2 they have sunk the battleship
      del player2InputRow #deletes player 2s input for row
      del player2InputCol #deletes player 2s input for col
      player2Wins += 1 #adds 1 to player 2s wins 
      print(player1 , "has " , player1Wins ," wins") #prints how many wins player 1 has
      print(player2 , "has " , player2Wins ," wins") #prints how many wins player 2 has
      coordinates = startGame(battleshipGrid) #Function is called upon to start the game
      playerWins() #calls on playerWins function
   elif player2InputRow > 6 or player2InputRow < 1 and player2InputCol > 6 or player2InputCol < 1: #else if statement for when inputs are not between 1 and 6
      print("Enter a number between 1 and 6") #prints a message that tells user to enter a number between 1 and 6
      player2Input() #calls on player2Input function
   else: #else statement
      print("Better luck next time!") #prints a statement for when answer is wrong
      player1Input() #calls on player 1 input function

coordinates = startGame(battleshipGrid) #Function is called upon to start the game 
         
player1Input() #calls on player 1 input function
   








    


    






