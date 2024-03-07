#Katheleen Hill
#5 March 2024
#P2HW1
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
location = 'Location:'
iBudget = 'Initial budget:'

locale = 'Asheville:'
budget = 1200.0
print('Location:           ' + str(location))
print('Initial budget:     $' + str(format(budget,',.1f')))                                                                                                                                                                                                        
print('Fuel:               $' + str(format(gas,',.1f')))
print('Accomodation:       $' + str(format(accomodation,',.1f')))
print('Food:               $' + str(format(food,',.1f')))
print('-'*40)
print('')
print('Remaining Balance:  $',budget-gas-accomodation-food)
##Pseudocode
## get the budget
## get the destination
## get the gas money
## get the money for the hotel
## get the food money
##Print the following: subtract the gas,food, and hotel expenses from the initial budget
