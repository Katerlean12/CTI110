#Katheleen Hill
#20 February 2024
#P1HW2
#This program will calculate travel expenses

print('This program calculates and displays travel expenses')
print("")
budget = int(input('Enter budget: '))
print("")
location = input('Enter your travel destination: ')
print("")
gas = int(input('How much do you think you will spend on gas? '))
print("")
accomodation = int(input('Approximately, how much will you need for accomodation/hotel? '))
print("")
food = int(input('Last, how much do you think you need for food? '))
print("")
print('------------Travel Expenses------------')

print('Location:',location)
print('Initial budget:',budget)
print("")
print('Fuel:',gas)
print('Accomodation:',accomodation)
print('Food:',food)
print("")
print('Remaining Balance:',budget-gas-accomodation-food)


##Pseudocode
## get the budget
## get the destination
## get the gas money
## get the money for the hotel
## get the food money
##Print the following: subtract the gas,food, and hotel expenses from the initial budget
