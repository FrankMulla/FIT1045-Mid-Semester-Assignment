#Code by Takudzwa Frank Mukarakate, Monash Student Id: 27754251
#This code accepts a positive integer number n and outputs an approximation for value "e"
#Using n + 1 terms

#Declaration of variables and arrays
finale = 0 # Represents the final number of "e"
temp = 0 # Keeps all the denominater parts for easy tracking of values

#Asking for input for "n"
n = int(input("Please enter a  positive integer value: "))

# The first value in temp would be the base number of all the denominator
temp = n + (n/(n+1))

#Calculates the demominater using the base temp and working its way to the final fraction
for i in range (1,n):
    temp =(n - i)+ ((n-i)/temp)

finale = 2 + 1/temp
# Outputing the final refined Euler's number
print(str(finale))

        
