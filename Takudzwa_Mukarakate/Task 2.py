#Code by: Takudzwa Frank Mukarakate, Monash Student Id: 27754251
#Assuming the input text file has a magic square either completed or partial!
#This piece of python code accepts input as a text file, processes the contents into a table(List of lists).
#The program then allows the user to input(edit empty spaces) and complete the magic square.
#making sure it still has the correct properties.


#Declaration and initialisation of variables
MagicSquare = [] #List of Lists that keeps the magic square contents
MagicSquareString = [] #Keeps the string and original version of the magic square
textFileName = "" #The variable containing the file name
EditDec = "" # This is either y for yes or n for norepresenting if the user wants to edit or not
MagicSumNum = 0 #This keeps the magic sum number
MagicInComp = 0 #This is 1(true) when the magic square is incomplete and 0(false) when its complete
Count = 0 #Keeps the count in some of the loops
Count2 = 0 #Keeps the count in some of the loops
SideCount = 0 #Keeps the length of the magic square
LineCount = 0 #Keeps track of row indices when converting list to string
DiagSelect = 0 #This is 0 when a non diagonal cell has been selected and greater one when the cell selected is a diagonal
OGRowSum = 0 #Keeps the sum of the selected row contents
OGColSum = 0 #Keeps the sum of the selected column contents
OGDiagOne = 0 #Keeps the sum of the main diagonal contents i.e \
OGDiagTwo = 0 #Keeps the sum of the main diagonal contents i.e /
InputErrorState = 0 # Is zero when there are no errors in the input and is 1 when theres an error
EditState = 0 #is zero when no part in the magic square has been change and is 1 when the square has been edited
RowNum = 0 #Keeps track of the row number selected
ColNum = 0 #Keeps track of the column number selected
NewString = "" #Keeps the string for the new file



#Asking for input of file name and Magic Sum
textFileName = input("Please enter filename to be opened including extension: ")
textFile = open(textFileName, 'r+') # r+ mode is a reading and writing mode
MagicSumNum = int(input("Please Enter Magic Sum number: "))

#Putting all the contents of the text file into a Table
for line in textFile:
        MagicSquare.append(line.split())
#The second list will keep the original string data without any strings attatched when edited
import copy
MagicSquareString = copy.deepcopy(MagicSquare)
SideCount = len(MagicSquare)

#Checking if the magic square has empty spaces
for sublists in MagicSquare:
    for Count in range(len(MagicSquare)):
        if sublists[Count] == "0":
            MagicInComp = 1
            break

#Replacement of empty spaces and navigation of the Square only if the list is Incomplete
if MagicInComp == 1:

        #Converts the magic square to numeric digits, the original string data is in table: MagicSquareString
        for sublists in MagicSquare:
                for count in range(len(MagicSquare)):
                        sublists[count] = int(sublists[count])

        while EditDec != "n" and EditDec != "y":

                for sublists in MagicSquare:
                        print(sublists)
                
                EditDec = input("Do you want to complete the Square?? (y/n): ")
                if EditDec != "n" and EditDec != "y":
                        print("ERROR - Please select using y(yes) or n(no)")
        while EditDec != "n":
                for sublists in MagicSquare:
                        print(sublists)

                RowNum = 0
                ColNum = 0
                
                while RowNum > SideCount or  RowNum < 1:
                        RowNum = int(input("Please Enter the row number of the cell you would like to edit(1 to "+ str(SideCount) +"): "))
                        if RowNum > SideCount or RowNum <= 0:
                                print("ERROR!! - Row number is out of limits i.e doesnt exist please try again")

                
                while ColNum >>SideCount or  ColNum < 1:
                        ColNum = int(input("Please Enter the column number(1 to "+ str(SideCount) + "): "))
                        if ColNum > SideCount or ColNum <= 0:
                                print("ERROR!! - Column number is out of limits i.e doesnt exist please try again")
                #Adjustments for numbers to pass first selections and match indices
                RowNum = RowNum-1
                ColNum = ColNum-1
                OGRowSum = 0
                OGColSum = 0
                OGDiagOne = 0
                OGDiagTwo = 0
                
                #Diagonal state assignment
                if SideCount%2 != 0  and RowNum == ColNum and ((RowNum + ColNum)== (SideCount - 1)):
                        DiagSelect = 3                         
                elif RowNum == ColNum:
                        DiagSelect = 1
                elif ((RowNum + ColNum)== (SideCount - 1)):
                        DiagSelect = 2
                else:
                        DiagSelect = 0
                        
                #Inputting and Checking of magix square edit(s)
                if MagicSquare[RowNum][ColNum] != 0:
                        print("ERROR - The cell isn't empty!! Please select an empty cell to edit")
                        EditDec = input("Do you want to select another Cell(y/n): ")
                else:
                        InputErrorState = 0
                        tempinput = int(input("Please enter the number to be inserted(i.e. non - zero digit): "))
                        ##Check Row
                        for count in range(SideCount):
                                OGRowSum = OGRowSum + MagicSquare[RowNum][count]
                                if (OGRowSum + tempinput) > MagicSumNum:
                                                InputErrorState = 1
                                                break
                        ##Check Column
                        for count in range(SideCount):
                                OGColSum = OGColSum + MagicSquare[count][ColNum]
                                if (OGColSum + tempinput) > MagicSumNum:
                                                InputErrorState = 1
                                                break
                        ##Check Diag
                        if DiagSelect != 0:
                                if DiagSelect == 1 or DiagSelect == 3:
                                        for count in range(SideCount):
                                                OGDiagOne = OGDiagOne + MagicSquare[count][count]
                                        #Verifying sum property
                                        if OGDiagOne + tempinput > MagicSumNum:
                                                InputErrorState = 1
                                if DiagSelect == 2 or DiagSelect == 3:
                                        count2 = (SideCount - 1)
                                        for count in range(SideCount):
                                                OGDiagTwo = OGDiagTwo + MagicSquare[count][count2]
                                                count2 = count2 - 1
                                        if OGDiagTwo + tempinput > MagicSumNum:
                                                InputErrorState = 1
                        if InputErrorState != 1:
                                MagicSquare[RowNum][ColNum]= tempinput
                                print("Square Updated!")
                                EditState = 1

                                #Check if the square is complete
                                MagicInComp = 0
                                for sublists in MagicSquare:
                                        for Count in range(len(MagicSquare)):
                                                if sublists[Count] == 0:
                                                        MagicInComp = 1
                                                        break
                                if MagicInComp == 0:
                                        EditDec = "n"
                                else:
                                        EditDec = input("The Square is still incomplete, would you like to add more values(y/n): ")
                        else:
                                print("Error!! - Either the row, column or diagonal sum(s) were exceeded - Invalid Input")
                                EditDec = input("Would you like to try again??(y/n): ")

                               
                                
        
    
       
if MagicInComp == 0:
        print("This Magic Square is complete")
        for sublists in MagicSquare:
                print(sublists)
else:
        print("The final square is: ")
        for sublists in MagicSquare:
                print(sublists)
if EditState == 1:
        print()
        print("The program detects that there were changes made to the square:")
        SaveDec = input("Would you like to save the changes into a new file??(y/n): ")
        
        if SaveDec == "y":
                NewFileName = input("What would you like to name your new file?: ")
                NewFile = open(NewFileName, "w")
                
                for sublists in MagicSquare:
                        for count in range(len(MagicSquare)):
                                NewString = NewString + str(sublists[count])
                                NewString = NewString + " "
                        NewString = NewString + "\n"
                NewFile.write(NewString)
                print("File Saved!")
                NewFile.close()
        
print("Thank You!!")
textFile.close()

input("Press Enter to Close the program")
exit()
