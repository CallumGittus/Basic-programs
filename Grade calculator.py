fName = str(input("What is your first name?"))                                             #Asks the user for their fisrt name then stores it in a variable called fName. input is saved as a string

sName = str(input("What is your second name?"))                                            #Asks the user for their second name then stores it in a varaible called sName. input is saved as a string

print("Hello" ,fName ,sName , "lets calculate your grade!")                                #Program says "hello" (then prints the fName and sName varaibles) "lets calculate your grade" 

numberOfModules = int(input("How many modules do you have during your academic studies?")) #Aks the user how many modules they have then stores the users input as an integer in the varaible numberOfModules 

#Program tells the user how many modules they have. It gets the information from the varaible numberOfModulesask then ask the user what their overall pass grade is. This is stored in the varaible minPassGrade and stored as an integer
minPassGrade = int(input("you have " + format(numberOfModules) + " modules during your academic studies. What is the overall pass grade for your course?"))

moduleGrades = []                                                                          #Stores the users module grades in a list

moduleNumber = 1                                                                           #A variable that tracks what module number the user is on for the while loop below. when it reachs greater than numberOfModules varaible the loop below ends.

while moduleNumber <= numberOfModules:                                                     #A while loop that runs until the module number is geater than number of modules. It gets the grade for each module whilst adding each grade to a list called moduleGrades
    userInput = int(input("Enter grade for module " + format(moduleNumber) + ":"))         #The program asks the user to "Enter grade for module" for the module the program is on from 1 till the users last module. The input gets saved in the varaible userInput but is replaced by the users next input so each input is saved into a list 
    moduleGrades.append(userInput)                                                         #This saves each of the values from userInput into a list with the .append command.
    moduleNumber = moduleNumber + 1                                                        #Adds 1 to the varabile moduleNumber so it reachs a high value than numberOfModules to stop the loop when each module has got its grade.

moduleNumber2 = 1                                                                          #A variable called moduleNumber2 is used to label each module grade in the for loop below

for x in moduleGrades:                                                                     #A for loop that loops equal to the amount of entitys in the list moduleNumber2. So if theres 9 it loops 9 times.  
    print("module " + str(moduleNumber2) + ":" + str(x))                                   #Prints each grade for each module from the list moduleGrades in a list. formatted as a string
    moduleNumber2 = moduleNumber2 + 1                                                      #Adds plus one to the varaible moduleNumber2 so the loop displays the right module number for each grade as the loop goes down the list.

total = sum(moduleGrades)                                                                  #Adds up all of the numbers in the list moduleGrades and stored in a varaible called total.

averageGrade = int(total / numberOfModules)                                                #Divides the total marks by the number of modules to get the average grade which is stored in the varaible averageGrade as an integer.

print("Your average grade is " + str(averageGrade))                                        #Tells the user their avarage grade. averageGrade is formatted as a string as print can only concatenate strings not integers.

if averageGrade >= minPassGrade:                                                           #An if statement saying if the average grade is higher or equal to the minimum pass grade, it tells the user they passed.
    print("Well Done",fName ,sName ,"You've passed your course")
else:                                                                                      #An else statement that tells the user they failed if their average grade was lower than the minimum pass grade.                                              
    print("Based on your grades you've failed your course. I'm sorry" ,fName ,sName)       











     




