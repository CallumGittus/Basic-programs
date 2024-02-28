import random #imports a random number generetor 

pinP1 = int(random.randint(1,100))#sets the variable to a random number between 1 and 100

pinP2 = int(random.randint(1,100))

livesP1 = 9 #used to track player 1s lives

livesP2 = 9 #used to track player 2s lives

n = 1 #used to keep the loop going

guessesP1 = [] #stores all of Player 1s guese in a list

guessesP2 = [] #stores all of Player 1s guese in a list


while n == 1 :#while n = 1 the loop will continue
    try:
        userInput1 = int(input("Player 1, enter a number between 1-100."))#ask the user to input a number between 1-100
    except ValueError: #except the value
        print("I didn't recognize that, type a number as a digit such as, 10") #tells the user that their input is wrong and to try again
        continue                                                              #starts again from the loop
    userInput2 = int(input("Player 2.enter a number between 1-100."))#ask the user to input a number between 1-100
    guessesP1.append(userInput1) #add each user input into a list
    guessesP2.append(userInput2) #add each user input into a list
    if userInput1 == pinP1: #if the users input equalls the pin, move onto another if statement
        guessesP1.clear()
        guessesP2.clear()
        playAgain = input("Well done Plyaer 1 thats correct.Press y to play again and n to stop.")# ask  for the user input to say if they want to play again. Y for yes, n for no
        if playAgain == ("y"):#if the user puts in y, the game restarts
            import random 
            pinP1 = random.randint(1,100)# sets a random new pin between 1 and a 100 and the loop continues
            pinP2 = random.randint(1,100)
            livesP1 = 9 #sets the lives back to 9
            livesP2 = 9
        elif playAgain == ("n"): #if the user puts n, game ends
            print("Thanks for playing.")
            livesP1 = 0 #sets the live to 0
            n = n + 1
    elif userInput2 == pinP2:
        guessesP1.clear()
        guessesP2.clear()
        playAgain = input("Well done Plyaer 2 thats correct.Press y to play again and n to stop.")# ask  for the user input to say if they want to play again. Y for yes, n for no
        if playAgain == ("y"): #if the user puts in y, the game restarts
            import random
            pinP1 = random.randint(1,100)# sets a random new pin between 1 and a 100 and the loop continues
            pinP2 = random.randint(1,100)
            livesP1 = 9 #sets the lives back to 9
            livesP2 = 9
        elif playAgain == ("n"): #if the user puts n, game ends
            print("Thanks for playing.")
            livesP1 = 0#sets the live to 0
            n = n + 1
    if livesP1 == 0:
        closestGuessP1 = min(guessesP1, key = lambda x:abs(x-pinP1))#compares the list to the pin then sets the closestGuess varable to the user closest guess
        closestGuessP2 = min(guessesP2, key = lambda x:abs(x-pinP2))
        print("You ran out of lives, game over. Player 1s  closest guess was:",closestGuessP1,"and player 2s closest guessis",closestGuessP2)# tells the user they lost and their closest guese
        guessesP1.clear()
        guessesP2.clear()
        playAgain2 = input("do you want to play again. Y for yes, N for no")
        if playAgain2 == ("y"):
            import random
            pinP1 = random.randint(1,100)# sets a random new pin between 1 and a 100 and the loop continues
            pinP2 = random.randint(1,100)
            livesP1 = 9 #sets the lives back to 10
            livesP2 = 9
        elif playAgain2 == ("n"): #if the user puts n, game ends
            print("Thanks for playing.")
            livesP1 = 0 #sets the live to 0
            liveP2 = 0
            n = n + 1 #stops the loop
    if userInput1 < pinP1:
        print ("Playr 1, the pin is a higher number.")#tells the user the pin is higher than their input
        livesP1 = livesP1 - 1
    elif userInput1 > pinP1:
        print ("Playr 1, the pin is a lower number.")
        livesP1 = livesP1 - 1
    if userInput2 < pinP2:
        print("Player 2, the pin is a higher number.")  #tells the user the pin is higher than their input
        livesP2 = livesP2 - 1
    elif userInput2 > pinP2:
        print("Player 2, the pin is a lower number.")
        livesP2 = livesP2 - 1
        


