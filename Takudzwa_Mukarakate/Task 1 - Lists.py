#Code by Takudzwa Frank Mukarakate, Monash Id: 27754251
#This code uses a list structure to store values calculated at each step
#This code accepts a positive integer number n and outputs an approximation for value "e" which represents Eulers Number
#Using n + 1 terms

#Declaration of variable(s) and List(s)
finale = 0 # Represents the final number of "e"
SumStack = [] # Keeps all the denominater parts for easy tracking of values

#Asking for input for "n"
n = int(input("Please Enter a  positive inter value: "))

#Creating the first element of the list which will the base denominator
#Float function is used just in case there are any errors with the class of the entry
SumStack.append(float(n + (n/(n+1))))

#Calculates the demominater using the list elements and works its way to the final fraction and calculates the final value after the loop
for i in range (1,n):
    print (str(n-1))
    print("Strin sum latest: " + str(SumStack[i-1]) + " Plus Number: " + str(n-i/SumStack[i-1]))
    SumStack.append((n - i)+ ((n-i)/SumStack[i-1]))

finale = 2 + 1/SumStack[i]

# Outputing the final refined Euler's number
print(str(finale))

        
